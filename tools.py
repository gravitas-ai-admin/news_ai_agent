from langchain_core.retrievers import BaseRetriever
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
import requests, os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import AzureChatOpenAI, ChatOpenAI, OpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


embedding_function = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'), model="text-embedding-3-large")
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4o")


# Tool 1 : Save the news articles in a database
class SearchNewsDB:
    @tool("News DB Tool")
    def news(query: str):
        """Fetch news articles and process their contents."""
        API_KEY = os.getenv('NEWSAPI_KEY')  # Fetch API key from getenvment variable
        base_url = "https://newsapi.org/v2/everything"
        
        params = {
            'q': query,
            'sortBy': 'publishedAt',
            'apiKey': API_KEY,
            'language': 'en',
            'pageSize': 1,
        }
        print('--------params',params)
        
        response = requests.get(base_url, params=params)
        print('-------------',response.status_code)
        if response.status_code != 200:
            return "Failed to retrieve news."
        
        articles = response.json().get('articles', [])
        all_splits = []
        for article in articles:
            # Assuming WebBaseLoader can handle a list of URLs
            loader = WebBaseLoader(article['url'])
            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)
            all_splits.extend(splits)  # Accumulate splits from all articles
        print('all_splits-------------', all_splits)
        # Index the accumulated content splits if there are any
        if all_splits:
            vectorstore = Chroma.from_documents(all_splits, embedding=embedding_function, persist_directory="./chroma_db")
            retriever = vectorstore.similarity_search(query)
            print('retriever-------------chromaDB stored')
            return retriever
        else:
            return "No content available for processing."

# Tool 2 : Get the news articles from the database
class GetNews:
    @tool("Get News Tool")
    def news(query: str) -> str:
        """Search Chroma DB for relevant news information based on a query."""
        vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)
        retriever = vectorstore.similarity_search(query)
        print('retriever-------------chromaDB retrieved')
        return retriever

# Tool 3 : Search for news articles on the web
search_tool = DuckDuckGoSearchRun()
