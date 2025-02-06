# 📰 Tina News Agent

## 📌 Overview
The **Tina News Agent** is an AI-powered system designed to fetch and summarize the latest news articles on a given topic. It leverages:
- **CrewAI** for agent-based orchestration 🤖
- **ChromaDB** for efficient vector storage and retrieval 🗄️
- **OpenAI GPT-4o** for intelligent summarization and analysis 🧠
- **DuckDuckGo Search API** to gather real-time news from various sources 🌎

This project enables users to quickly receive concise, high-quality summaries of recent news articles on their desired topics.

---

## ⚙️ Features
- 🔍 **Search & Retrieve:** Fetches the latest news from diverse sources.
- 🏛️ **Vector Storage:** Uses ChromaDB to store and retrieve processed news efficiently.
- 📝 **AI Summarization:** Condenses lengthy articles into brief, insightful summaries using GPT-4o.
- 📈 **Trending Insights:** Identifies key trends and provides contextual understanding.
- 📡 **Real-time Updates:** Ensures access to the latest news by continuously fetching fresh content.

---

## 🏗️ Tech Stack
- **[CrewAI](https://github.com/joaomdmoura/crewai)** – Agent-based AI task delegation
- **[ChromaDB](https://www.trychroma.com/)** – High-performance vector database
- **[OpenAI GPT-4o](https://openai.com/research/gpt-4o)** – AI model for summarization
- **[DuckDuckGo Search API](https://duckduckgo.com/api)** – News aggregation API
- **Python 3.10+** – Core programming language

---

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/gravitas-ai-admin/news_ai_agent.git
cd news_ai_agent
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.10+ installed, then run:
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
Create a `.env` file and add your API keys:
```env
OPENAI_API_KEY=your_openai_key
DUCKDUCKGO_API_KEY=your_duckduckgo_key
CHROMADB_PATH=./chroma_db
```

### 4️⃣ Run the News Agent
```sh
python tools.py --topic "Your Topic Here"
```

---

## 🎯 Usage
### Fetch & Summarize News
Run the agent with a topic of interest to retrieve and summarize news:
```sh
python tools.py --topic "Artificial Intelligence"
```
### Expected Output
```
Fetching news on: Artificial Intelligence...
Summarizing articles...
✅ Summary:
1️⃣ AI advancements in healthcare...
2️⃣ OpenAI releases new model...
3️⃣ Governments regulate AI ethics...
```

---

## 🔥 Future Enhancements
- 🗣️ Voice-enabled news summaries
- 📺 Video summary generation
- 📡 Real-time push notifications
- 🔄 Multi-language support

---

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Open issues 🐞
- Submit PRs 📌
- Suggest improvements 🚀

---


