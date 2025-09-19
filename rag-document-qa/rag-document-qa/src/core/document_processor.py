"""
Document processing module for PDF text extraction and chunking
"""
import os
from typing import List, Dict
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from tqdm import tqdm


class DocumentProcessor:
    """Handles PDF processing and text chunking"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from PDF file"""
        try:
            reader = PdfReader(pdf_path)
            text = ""
            
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Page {page_num + 1} ---\n{page_text}"
            
            return text
        except Exception as e:
            print(f"Error reading {pdf_path}: {str(e)}")
            return ""
    
    def process_documents(self, pdf_directory: str) -> List[Document]:
        """Process all PDFs in directory"""
        documents = []
        pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
        
        if not pdf_files:
            print(f"No PDF files found in {pdf_directory}")
            return documents
        
        print(f"Processing {len(pdf_files)} PDF files...")
        
        for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            text = self.extract_text_from_pdf(pdf_path)
            
            if text:
                # Create chunks
                chunks = self.text_splitter.split_text(text)
                
                # Create Document objects with metadata
                for i, chunk in enumerate(chunks):
                    doc = Document(
                        page_content=chunk,
                        metadata={
                            "source": pdf_file,
                            "chunk_index": i,
                            "total_chunks": len(chunks)
                        }
                    )
                    documents.append(doc)
        
        print(f"Created {len(documents)} document chunks")
        return documents


# Test function
if __name__ == "__main__":
    processor = DocumentProcessor()
    
    # Create test directory if it doesn't exist
    test_dir = "./data/raw"
    os.makedirs(test_dir, exist_ok=True)
    
    print("Document processor created successfully!")
    print(f"Place PDF files in: {os.path.abspath(test_dir)}")
