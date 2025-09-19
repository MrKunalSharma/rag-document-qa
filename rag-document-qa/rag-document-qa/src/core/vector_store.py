"""
Vector store module using ChromaDB for document embeddings and retrieval
"""
import os
from typing import List, Dict, Optional
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

from dotenv import load_dotenv
import chromadb

load_dotenv()


class VectorStore:
    """Handles vector storage and retrieval using ChromaDB"""
    
    def __init__(self, 
                 persist_directory: str = "./data/chromadb",
                 embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize vector store
        
        Args:
            persist_directory: Directory to persist ChromaDB
            embedding_model: HuggingFace model for embeddings
        """
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        
        # Initialize embeddings
        print(f"Loading embedding model: {embedding_model}")
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Initialize or load vector store
        self.vector_store = None
        
    def create_vector_store(self, documents: List[Document]) -> Chroma:
        """Create vector store from documents"""
        print(f"Creating vector store with {len(documents)} documents...")
        
        # Create ChromaDB instance
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            collection_name="rag_documents"
        )
        
        # Persist the database
        self.vector_store.persist()
        print(f"Vector store created and persisted to {self.persist_directory}")
        
        return self.vector_store
    
    def load_vector_store(self) -> Optional[Chroma]:
        """Load existing vector store"""
        try:
            self.vector_store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings,
                collection_name="rag_documents"
            )
            print(f"Loaded vector store from {self.persist_directory}")
            return self.vector_store
        except Exception as e:
            print(f"No existing vector store found: {str(e)}")
            return None
    
    def similarity_search(self, query: str, k: int = 5) -> List[Document]:
        """Search for similar documents"""
        if not self.vector_store:
            print("Vector store not initialized!")
            return []
        
        results = self.vector_store.similarity_search(query, k=k)
        return results
    
    def similarity_search_with_score(self, query: str, k: int = 5) -> List[tuple]:
        """Search with relevance scores"""
        if not self.vector_store:
            print("Vector store not initialized!")
            return []
        
        results = self.vector_store.similarity_search_with_score(query, k=k)
        return results
    
    def get_retriever(self, search_kwargs: Optional[Dict] = None):
        """Get retriever for chain"""
        if not self.vector_store:
            raise ValueError("Vector store not initialized!")
        
        search_kwargs = search_kwargs or {"k": 5}
        return self.vector_store.as_retriever(search_kwargs=search_kwargs)


# Test function
if __name__ == "__main__":
    from document_processor import DocumentProcessor
    
    # Process documents
    processor = DocumentProcessor()
    documents = processor.process_documents("../../data/raw")

    
    if documents:
        # Create vector store
        vector_store = VectorStore()
        vector_store.create_vector_store(documents)
        
        # Test search
        test_query = "What is the transformer architecture?"
        print(f"\nTesting search with query: '{test_query}'")
        
        results = vector_store.similarity_search_with_score(test_query, k=3)
        
        print(f"\nFound {len(results)} relevant chunks:")
        for i, (doc, score) in enumerate(results):
            print(f"\n--- Result {i+1} (Score: {score:.4f}) ---")
            print(f"Source: {doc.metadata['source']}")
            print(f"Content: {doc.page_content[:200]}...")
    else:
        print("No documents to process!")
