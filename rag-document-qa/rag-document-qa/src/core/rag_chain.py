"""
RAG Chain module that combines retrieval and generation
"""
import os
from typing import Dict, List, Optional
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

from dotenv import load_dotenv
from src.core.vector_store import VectorStore
from src.core.document_processor import DocumentProcessor


load_dotenv()


class RAGChain:
    """Main RAG chain for question answering"""
    
    def __init__(self, 
                 model_name: str = "gpt-3.5-turbo",
                 temperature: float = 0.7,
                 max_tokens: int = 500):
        """
        Initialize RAG chain
        
        Args:
            model_name: OpenAI model to use
            temperature: Temperature for generation
            max_tokens: Maximum tokens in response
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # Initialize components
        self.vector_store = VectorStore()
        self.document_processor = DocumentProcessor()
        
        # Load or create vector store
        if not self.vector_store.load_vector_store():
            print("No existing vector store found. Please process documents first.")
        
        # Initialize LLM (we'll use a mock for now if no API key)
        api_key = os.getenv("OPENAI_API_KEY", "dummy_key")
        self.llm = self._initialize_llm(api_key)
        
        # Create QA chain
        self.qa_chain = None
        self._create_qa_chain()
    
    def _initialize_llm(self, api_key: str):
        """Initialize the language model"""
        if api_key == "dummy_key":
            # For testing without API key
            print("⚠️  No OpenAI API key found. Using mock responses for testing.")
            return None
        else:
            return ChatOpenAI(
                model_name=self.model_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                openai_api_key=api_key,
                streaming=True,
                callbacks=[StreamingStdOutCallbackHandler()]
            )
    
    def _create_qa_chain(self):
        """Create the QA chain with custom prompt"""
        if not self.vector_store.vector_store:
            print("Vector store not initialized!")
            return
        
        # Custom prompt template
        prompt_template = """You are a helpful AI assistant. Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Always cite which document your answer comes from.

Context:
{context}

Question: {question}

Answer:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        if self.llm:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.get_retriever(),
                return_source_documents=True,
                chain_type_kwargs={"prompt": PROMPT}
            )
        else:
            # Mock chain for testing
            self.qa_chain = None
    
    def process_new_documents(self, pdf_directory: str):
        """Process new documents and update vector store"""
        documents = self.document_processor.process_documents(pdf_directory)
        if documents:
            self.vector_store.create_vector_store(documents)
            self._create_qa_chain()
            return len(documents)
        return 0
    
    def query(self, question: str) -> Dict:
        """Query the RAG system"""
        if not self.qa_chain:
            # Mock response for testing without OpenAI API
            similar_docs = self.vector_store.similarity_search(question, k=3)
            
            response = {
                "query": question,
                "result": f"[Mock Response] Based on the documents, here's what I found about '{question}':\n\n",
                "source_documents": similar_docs
            }
            
            if similar_docs:
                response["result"] += f"From {similar_docs[0].metadata['source']}:\n"
                response["result"] += f"{similar_docs[0].page_content[:300]}..."
            else:
                response["result"] = "No relevant information found in the documents."
            
            return response
        
        # Real query with OpenAI
        try:
            response = self.qa_chain({"query": question})
            return response
        except Exception as e:
            return {
                "query": question,
                "result": f"Error: {str(e)}",
                "source_documents": []
            }
    
    def get_relevant_chunks(self, question: str, k: int = 5) -> List[Dict]:
        """Get relevant chunks with scores"""
        results = self.vector_store.similarity_search_with_score(question, k=k)
        
        chunks = []
        for doc, score in results:
            chunks.append({
                "content": doc.page_content,
                "source": doc.metadata.get("source", "Unknown"),
                "score": float(score),
                "chunk_index": doc.metadata.get("chunk_index", -1)
            })
        
        return chunks


# Test function
if __name__ == "__main__":
    # Initialize RAG chain
    rag = RAGChain()
    
    # Test queries
    test_questions = [
        "What is the transformer architecture?",
        "How does BERT work?",
        "What is the attention mechanism?",
        "Explain GPT-3 capabilities"
    ]
    
    print("RAG Chain Test\n" + "="*50)
    
    for question in test_questions:
        print(f"\n🤔 Question: {question}")
        print("-" * 50)
        
        # Get response
        response = rag.query(question)
        
        print(f"💡 Answer: {response['result'][:500]}...")
        
        if response.get('source_documents'):
            print(f"\n📚 Sources:")
            for doc in response['source_documents'][:2]:
                print(f"  - {doc.metadata['source']}")
        
        print("\n" + "="*50)
