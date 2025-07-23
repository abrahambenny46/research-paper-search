# 🔍 Research Paper Search Engine

A full-stack web application that allows users to search academic papers using natural language queries. It fetches relevant research papers from **arXiv**, uses **semantic search** to rank them, and generates **AI-powered summaries** of each paper’s key findings — all in real time and optimized to run on CPU.



---

## 🚀 Features

-  Search scholarly papers using plain language
-  Fetches real-time papers from **arXiv API**
-  Uses **vector embeddings** for semantic search
-  Generates **short AI summaries** for each paper
-  Optimized for **CPU-only environments**
-  Built with **Flask**


---

## 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | Flask (Jinja2), HTML, Bootstrap 5 |
| Backend      | Flask, REST routing |
| Embeddings   | SentenceTransformers (MiniLM) |
| Summarization| HuggingFace Transformers (DistilBART) |
| Search Engine| FAISS (CPU version) |
| Data Source  | arXiv API |

---

# 📁 Project Structure
research_paper_search/
│
├── app.py # Flask app 
├── fetch_papers.py # Gets papers from arXiv
├── embedder.py # Embeds text into vectors
├── summarizer.py # Summarizes paper abstracts
├── search_engine.py # FAISS search logic
├── requirements.txt # Python dependencies
└── templates/
└── index.html # Frontend UI


---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/abrahambenny46/research-paper-search.git
cd research-paper-search
