from crewai import Agent
import requests, os
from langchain_openai import AzureChatOpenAI, ChatOpenAI, OpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
from tools import SearchNewsDB, GetNews, search_tool
from dotenv import load_dotenv

load_dotenv()

embedding_function = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'), model="text-embedding-3-large")
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4o")

news_search_agent = Agent(
    role='News Seacher',
    goal='Generate key points for each news article from the latest news',
    backstory='Expert in analysing and generating key points from news content for quick updates.',
    tools=[SearchNewsDB().news],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

writer_agent = Agent(
    role='Writer',
    goal='Identify all the topics received. Use the Get News Tool to verify the each topic to search. Use the Search tool for detailed exploration of each topic. Summarise the retrieved information in depth for every topic.',
    backstory='Expert in crafting engaging narratives from complex information.',
    tools=[GetNews().news, search_tool],
    allow_delegation=True,
    verbose=True,
    llm=llm
)
