# RAG Document Q&A System

A production-ready Retrieval-Augmented Generation (RAG) system that enables intelligent question-answering over PDF documents using semantic search and natural language processing.

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

[Live Demo](https://rag-document-app-n9nrripappuptgnnafem92v.streamlit.app/) | [Documentation](#api-documentation)

## Features

- **Semantic Search**: Find relevant information using natural language queries, not just keywords
- **Multi-Document Support**: Process and search across multiple PDF files simultaneously
- **Real-time Processing**: Sub-second query response times with efficient vector search
- **Dual Mode Operation**: Works with or without OpenAI API for flexibility
- **RESTful API**: Well-documented API endpoints for easy integration
- **Persistent Storage**: ChromaDB vector database with 425+ indexed document chunks
- **Interactive UI**: Beautiful Streamlit interface with real-time results

## Architecture

The system follows a modular architecture:

- **Frontend**: Streamlit UI for user interactions
- **Backend**: FastAPI server handling requests
- **Vector Store**: ChromaDB for semantic search
- **Processing Pipeline**: LangChain for document processing and RAG

## Live Demo

[Try the Live Demo Here](https://rag-document-app-n9nrripappuptgnnafem92v.streamlit.app/)

### Demo Features
- Interactive search interface
- Sample questions for quick testing
- File upload demonstration
- Performance analytics
- Technical architecture details

## Performance Metrics

| Metric | Value | Description |
|--------|-------|-------------|
| Query Response Time | < 1 second | End-to-end search latency |
| Document Chunks | 425+ | Searchable text segments |
| Embedding Dimensions | 384 | Using all-MiniLM-L6-v2 |
| Similarity Accuracy | 87.8% | Relevance score threshold |
| Chunk Size | 1000 chars | Optimal context preservation |
| Chunk Overlap | 200 chars | Ensures continuity |

## Tech Stack

- **Backend**: FastAPI, LangChain, ChromaDB
- **Frontend**: Streamlit
- **ML/AI**: Sentence Transformers, HuggingFace Embeddings
- **Storage**: ChromaDB (Persistent Vector Store)
- **Processing**: PyPDF for document extraction
- **Optional**: OpenAI API for enhanced generation

## Prerequisites

- Python 3.9 or higher
- pip package manager
- (Optional) OpenAI API key for full RAG functionality

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MrKunalSharma/rag-document-qa.git
cd rag-document-qa/rag-document-qa
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables (optional):**
```bash
# Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Running the Complete System

### Start the Backend API:
```bash
python src/api/main.py
```
The API will be available at http://localhost:8000

### Start the Frontend (new terminal):
```bash
streamlit run src/frontend/app.py
```
Access the UI at http://localhost:8501

## Project Structure

```
rag-document-qa/
├── data/
│   ├── raw/                 # Original PDF documents
│   └── chromadb/           # Vector database (425+ chunks)
├── src/
│   ├── api/
│   │   └── main.py         # FastAPI backend server
│   ├── core/
│   │   ├── document_processor.py  # PDF processing pipeline
│   │   ├── rag_chain.py          # RAG orchestration
│   │   └── vector_store.py       # ChromaDB integration
│   └── frontend/
│       └── app.py          # Streamlit UI
├── requirements.txt        # Project dependencies
├── .env.example           # Environment variables template
└── README.md             # This file
```

## API Documentation

### Health Check
```http
GET /health
```

### Search Endpoint (No LLM Required)
```http
POST /search
Content-Type: application/json

{
    "question": "How does self-attention work?",
    "num_results": 5
}
```

### Query Endpoint (Full RAG with Optional LLM)
```http
POST /query
Content-Type: application/json

{
    "question": "Explain the transformer architecture",
    "num_results": 3
}
```

### Response Format
```json
{
    "question": "How does self-attention work?",
    "answer": "Based on the search results...",
    "sources": [
        {
            "source": "attention_is_all_you_need.pdf",
            "content": "Self-attention is an attention mechanism...",
            "score": "0.878"
        }
    ]
}
```

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| chunk_size | 1000 | Characters per chunk |
| chunk_overlap | 200 | Overlap between chunks |
| embedding_model | all-MiniLM-L6-v2 | HuggingFace model |
| vector_dimensions | 384 | Embedding dimensions |
| similarity_metric | cosine | Distance calculation |

## Use Cases

- **Academic Research**: Search through research papers and citations
- **Legal Documentation**: Find relevant cases and precedents
- **Healthcare**: Search medical literature and patient records
- **Enterprise Knowledge Base**: Internal documentation search
- **Educational Content**: Smart library and course material search

## Future Enhancements

- [ ] Multi-language support
- [ ] GPU acceleration for embeddings
- [ ] Real-time document upload via API
- [ ] Advanced filtering options
- [ ] Export results to various formats
- [ ] User authentication and management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Kunal Sharma**

- GitHub: [@MrKunalSharma](https://github.com/MrKunalSharma)
- LinkedIn: [Kunal Sharma](https://www.linkedin.com/in/kunal-sharma-1a8457257/)
- Email: kunalsharma13579kunals@gmail.com

## Acknowledgments

- LangChain for the excellent RAG framework
- Sentence Transformers team for the embedding models
- ChromaDB for the vector database
- Streamlit for the amazing UI framework

---

Built with ❤️ for the AI community
⭐ Star this repo if you find it helpful!
