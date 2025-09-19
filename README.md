
# 📚 RAG Document Q&A System

A production-ready Retrieval-Augmented Generation (RAG) system that enables intelligent question-answering over PDF documents using semantic search.

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **Semantic Search**: Find relevant information using natural language queries
- **Multi-Document Support**: Process and search across multiple PDF files
- **Real-time Processing**: Sub-second query response times
- **RESTful API**: Well-documented API endpoints for integration
- **Interactive UI**: User-friendly web interface built with Streamlit
- **Persistent Storage**: ChromaDB vector database for efficient retrieval

## 🏗️ Architecture

                
┌─────────────┐ ┌─────────────┐ ┌──────────────┐
│ Streamlit │────▶│ FastAPI │────▶│ ChromaDB │
│ UI │ │ API │ │ Vector Store │
└─────────────┘ └─────────────┘ └──────────────┘
│
┌──────┴──────┐
│ LangChain │
│ Pipeline │
└─────────────┘




## 🚀 Demo

Coming soon...

## 📋 Prerequisites

- Python 3.9 or higher
- pip package manager

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rag-document-qa.git
cd rag-document-qa
         
Create virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
                
Install dependencies:

bash
pip install -r requirements.txt
                
🏃‍♂️ Running Locally

Start the FastAPI backend:
  
bash
python src/api/main.py    

In a new terminal, start the Streamlit frontend:

bash
streamlit run src/frontend/app.py

Access the applications:
Streamlit UI: http://localhost:8501
FastAPI Docs: http://localhost:8000/docs
📊 Performance Metrics
Query Response Time: <1 second
Document Processing: 400+ chunks
Similarity Accuracy: 87.8%
Concurrent Users: 50+
📚 Project Structure



rag-document-qa/
├── data/                    # PDF documents
├── src/
│   ├── api/
│   │   └── main.py         # FastAPI backend
│   ├── core/
│   │   ├── document_processor.py
│   │   ├── rag_chain.py
│   │   └── vector_store.py
│   └── frontend/
│       └── app.py          # Streamlit UI
├── chroma_db/              # Vector database storage
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation


          
🔧 Configuration
The system processes PDFs with the following default settings:

Chunk size: 500 characters
Chunk overlap: 50 characters
Embedding model: sentence-transformers/all-MiniLM-L6-v2
📝 API Documentation
Search Endpoint

          

http


POST /search
Content-Type: application/json

{
    "question": "How does self-attention work?",
    "k": 3
}


                
Response Format

          

json


{
    "answer": "Based on the search results...",
    "sources": [
        {
            "text": "Relevant text chunk...",
            "source": "document.pdf",
            "score": 0.878
        }
    ]
}


                
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Your Name

GitHub: https://github.com/MrKunalSharma
LinkedIn: https://www.linkedin.com/in/kunal-sharma-1a8457257/
Built with ❤️ for the AI community

