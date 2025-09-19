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
