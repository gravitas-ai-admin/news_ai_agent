from crewai import Crew, Process
from langchain_openai import AzureChatOpenAI, OpenAIEmbeddings, ChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
import requests, os
from dotenv import load_dotenv
from tasks import news_search_task, writer_task
from agents import news_search_agent, writer_agent

load_dotenv()

embedding_function = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'), model="text-embedding-3-large")
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4o")

# 4. Creating Crew
news_crew = Crew(
    agents=[news_search_agent, writer_agent],
    tasks=[news_search_task, writer_task],
    process=Process.sequential, 
    manager_llm=llm
)

# Execute the crew to see RAG in action
result = news_crew.kickoff()
print(result)