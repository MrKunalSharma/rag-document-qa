"""
Simplified RAG app for Hugging Face deployment
"""
import streamlit as st
import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG Document Q&A System")

# Show a demo interface without heavy backend
st.markdown("""
### Welcome to the RAG Document Q&A System!

This is a demonstration of a Retrieval-Augmented Generation system for intelligent document search.

**Features:**
- 🔍 Semantic search across PDF documents
- ⚡ Real-time question answering
- 📊 Relevance scoring
- 🎯 Source attribution
""")

# Create demo interface
col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input("Ask a question:", placeholder="How does self-attention work?")
    
    if st.button("Search", type="primary"):
        with st.spinner("Searching..."):
            # Show demo results
            st.success("✅ Search completed!")
            
            # Demo results
            st.markdown("### Results")
            
            with st.expander("📄 Result 1 (Score: 0.878)", expanded=True):
                st.write("Self-attention is a mechanism that relates different positions of a sequence...")
                st.caption("Source: attention_is_all_you_need.pdf")
            
            with st.expander("📄 Result 2 (Score: 0.823)"):
                st.write("The transformer uses multi-head attention in three different ways...")
                st.caption("Source: attention_is_all_you_need.pdf")

with col2:
    st.markdown("### Quick Links")
    st.markdown("""
    - 📂 [GitHub Repository](https://github.com/MrKunalSharma/rag-document-qa)
    - 🚀 [API Documentation](https://github.com/MrKunalSharma/rag-document-qa#api-documentation)
    - 💻 [Run Locally](https://github.com/MrKunalSharma/rag-document-qa#running-locally)
    """)
    
    st.info("""
    **Note**: This is a demo version. 
    
    For full functionality with actual document processing, please run locally.
    """)

# Add information section
with st.expander("ℹ️ About this Project"):
    st.markdown("""
    This RAG system processes PDF documents and enables intelligent Q&A using:
    - **LangChain** for document processing
    - **ChromaDB** for vector storage
    - **Sentence Transformers** for embeddings
    - **FastAPI** for backend API
    - **Streamlit** for UI
    
    The full version includes:
    - Real-time PDF processing
    - Semantic search with embeddings
    - RESTful API endpoints
    - Persistent vector storage
    """)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit • LangChain • ChromaDB")
