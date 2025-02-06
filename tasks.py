from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_core.retrievers import BaseRetriever
from langchain_openai import OpenAIEmbeddings
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
import requests, os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import AzureChatOpenAI, ChatOpenAI, OpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
from agents import news_search_agent, writer_agent
from tools import SearchNewsDB, GetNews, search_tool
from dotenv import load_dotenv
load_dotenv()


embedding_function = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'), model="text-embedding-3-large")
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4o")

news_search_task = Task(
    description='Search for DeepSeek  and create key points for each news.',
    agent=news_search_agent,
    tools=[SearchNewsDB().news],
    expected_output='A list of key points for each news article.'
)

writer_task = Task(
    description="""
    Go step by step.
    Step 1: Identify all the topics received.
    Step 2: Use the Get News Tool to verify the each topic by going through one by one.
    Step 3: Use the Search tool to search for information on each topic one by one. 
    Step 4: Go through every topic and write an in-depth summary of the information retrieved.
    Don't skip any topic.
    """,
    agent=writer_agent,
    context=[news_search_task],
    tools=[GetNews().news, search_tool],
    expected_output="""
    A detailed and comprehensive summary that thoroughly examines each topic, reflecting an in-depth analysis of the information retrieved. The summary should include the key points, relevant details, and significant insights from each news article or search result. Each topic must be covered with precision, ensuring that all relevant aspects are addressed and clearly articulated.
    """
)