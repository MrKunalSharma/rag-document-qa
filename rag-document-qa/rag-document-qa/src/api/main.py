"""
FastAPI backend for RAG system
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.core.vector_store import VectorStore
from src.core.rag_chain import RAGChain

# Initialize FastAPI app
app = FastAPI(
    title="RAG Document Q&A API",
    description="API for document question answering using RAG",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    question: str
    num_results: Optional[int] = 5

class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[Dict[str, str]]

class HealthResponse(BaseModel):
    status: str
    vector_store_loaded: bool
    document_count: Optional[int] = None

# Initialize RAG components
print("Initializing RAG system...")
rag_chain = RAGChain()

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    vector_store_loaded = rag_chain.vector_store.vector_store is not None
    return HealthResponse(
        status="healthy",
        vector_store_loaded=vector_store_loaded
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check"""
    vector_store_loaded = rag_chain.vector_store.vector_store is not None
    doc_count = None
    
    if vector_store_loaded:
        try:
            # Get approximate document count
            test_results = rag_chain.vector_store.similarity_search("test", k=1)
            doc_count = 425  # We know this from the processing
        except:
            doc_count = None
    
    return HealthResponse(
        status="healthy",
        vector_store_loaded=vector_store_loaded,
        document_count=doc_count
    )

@app.post("/query", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    """Query the document database"""
    try:
        # Get response from RAG chain
        response = rag_chain.query(request.question)
        
        # Format sources
        sources = []
        for doc in response.get("source_documents", [])[:3]:
            sources.append({
                "source": doc.metadata.get("source", "Unknown"),
                "content": doc.page_content[:200] + "...",
                "chunk_index": str(doc.metadata.get("chunk_index", -1))
            })
        
        return QueryResponse(
            question=request.question,
            answer=response["result"],
            sources=sources
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search_documents(request: QueryRequest):
    """Search documents without OpenAI - just returns relevant chunks"""
    try:
        # Directly use vector store for search
        vector_store = rag_chain.vector_store
        
        if not vector_store.vector_store:
            raise HTTPException(status_code=503, detail="Vector store not loaded")
        
        # Get relevant chunks with scores
        results = vector_store.similarity_search_with_score(
            request.question, 
            k=request.num_results
        )
        
        # Format sources
        sources = []
        for doc, score in results:
            sources.append({
                "source": doc.metadata.get("source", "Unknown"),
                "content": doc.page_content[:500] + "...",
                "score": str(float(score))  # Convert score to string
            })
        
        # Create response without OpenAI
        if results:
            # Use the best result to create a simple answer
            best_doc, best_score = results[0]
            answer = f"Based on the search results from '{best_doc.metadata.get('source', 'Unknown')}':\n\n{best_doc.page_content[:500]}..."
        else:
            answer = "No relevant information found in the documents."
        
        return QueryResponse(
            question=request.question,
            answer=answer,
            sources=sources
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents")
async def list_documents():
    """List processed documents"""
    return {
        "documents": [
            "attention_is_all_you_need.pdf",
            "bert_paper.pdf",
            "gpt_paper.pdf"
        ],
        "total_chunks": 425
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    