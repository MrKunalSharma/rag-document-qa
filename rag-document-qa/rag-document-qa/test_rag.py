"""
Test script for RAG system
"""
import sys
import os

# Add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from core.vector_store import VectorStore
from core.document_processor import DocumentProcessor

def test_system():
    print("Testing RAG System Setup\n" + "="*50)
    
    # Test 1: Check if vector store exists
    vector_store = VectorStore()
    if vector_store.load_vector_store():
        print("✅ Vector store loaded successfully!")
        
        # Test 2: Simple search
        test_query = "What is transformer?"
        results = vector_store.similarity_search(test_query, k=2)
        
        print(f"\n🔍 Test Query: '{test_query}'")
        print(f"Found {len(results)} relevant chunks\n")
        
        for i, doc in enumerate(results):
            print(f"Result {i+1}:")
            print(f"Source: {doc.metadata['source']}")
            print(f"Content preview: {doc.page_content[:150]}...\n")
    else:
        print("❌ No vector store found. Let's check if PDFs were processed...")
        
        # Check if we have PDFs
        pdf_dir = "./data/raw"
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
        print(f"Found {len(pdf_files)} PDF files in {pdf_dir}")
        
        if pdf_files:
            print("\nProcessing documents now...")
            processor = DocumentProcessor()
            documents = processor.process_documents(pdf_dir)
            
            if documents:
                vector_store.create_vector_store(documents)
                print("\n✅ Vector store created! Run the test again.")

if __name__ == "__main__":
    test_system()
