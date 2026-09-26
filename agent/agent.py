import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()
class Agent:
    def __init__(self, tools : list, alias : str, system_prompt : str = "You are a helpful AI assistant. /no_think"):
        self.tools = tools
        self.alias = alias
        self.system = SystemMessage(system_prompt)
        self.client = self._get_client().bind_tools(self.tools)
        self.graph = self.build_graph()
    
    def _get_client(self) -> ChatOpenAI:
        return ChatOpenAI(
            base_url=os.environ["LITELLM_BASE_URL"],
            api_key=os.environ["LITELLM_API_KEY"],
            model=self.alias,
            temperature=0.7,
        )

    def _call_model(self, state : MessagesState):
        response = self.client.invoke([self.system] + state["messages"])
        return {"messages": [response]}

    
    def build_graph(self):
        builder = StateGraph(MessagesState)
        builder.add_node("agent", self._call_model)
        builder.add_node("tools", ToolNode(self.tools))
        builder.add_edge(START, "agent")
        builder.add_conditional_edges("agent", tools_condition)
        builder.add_edge('tools', "agent")
        return builder.compile()

    def run(self, prompt: str, recursion_limit: int = 10):
        inputs = {"messages": [("user", prompt)]}
        config = {"recursion_limit": recursion_limit}
        for chunk in self.graph.stream(inputs, config, stream_mode="updates"):
            for node, update in chunk.items():
                print(f"--- {node} ---")
                update["messages"][-1].pretty_print()
