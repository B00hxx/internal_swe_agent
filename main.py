from agent import Agent
from tools.represent_repo import represent_repo

if __name__ == "__main__":
    Agent(tools=[represent_repo], 
          alias="qwen-with-tools").run("Describe this repo we are at ./fake_repo.")