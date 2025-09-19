"""
Process documents and create vector store
"""
import os
import sys
sys.path.append("src")

from core.document_processor import DocumentProcessor
from core.vector_store import VectorStore

def main():
    # Process documents
    print("Processing documents...")
    processor = DocumentProcessor()
    documents = processor.process_documents("./data/raw")
    
    if documents:
        # Create vector store
        print("\nCreating vector store...")
        vector_store = VectorStore()
        vector_store.create_vector_store(documents)
        
        # Test search
        print("\nTesting search...")
        results = vector_store.similarity_search("What is attention mechanism?", k=3)
        print(f"Found {len(results)} results")
        
        if results:
            print(f"\nFirst result from: {results[0].metadata['source']}")
            print(f"Content: {results[0].page_content[:200]}...")
    else:
        print("No documents found to process!")

if __name__ == "__main__":
    main()
