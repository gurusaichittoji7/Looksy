from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

# Tool
search_tool = TavilySearchResults(max_results=5)
tools = [search_tool]

# LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Agent
agent_executor = create_react_agent(llm, tools)

def run_search(query: str) -> str:
    result = agent_executor.invoke({"messages": [{"role": "user", "content": query}]})
    return result["messages"][-1].content