import streamlit as st

st.set_page_config(page_title="RAG Document Q&A", page_icon="📚")

st.title("📚 RAG Document Q&A System")
st.markdown("### AI-Powered Document Search & Question Answering")

# Introduction
st.markdown("""
This is a demonstration of a **Retrieval-Augmented Generation (RAG)** system that enables intelligent question-answering over PDF documents.

**Key Features:**
- 📄 PDF document processing
- 🔍 Semantic search using embeddings
- 💬 Natural language queries
- ⚡ Fast retrieval with vector database
- 🎯 Source attribution for answers
""")

# Demo interface
st.markdown("---")
st.markdown("### Try It Out")
query = st.text_input("Ask a question about your documents:", placeholder="How does self-attention work?")

if st.button("Search", type="primary"):
    with st.spinner("Searching..."):
        import time
        time.sleep(1)  # Simulate search
        
        st.success("✅ Search completed!")
        
        # Show demo results
        st.markdown("### 📊 Search Results")
        
        with st.expander("📄 Result 1 - Attention Is All You Need (Score: 87.8%)", expanded=True):
            st.markdown("""
            **Relevant excerpt:**
            > Self-attention, sometimes called intra-attention, is an attention mechanism relating different positions 
            > of a single sequence in order to compute a representation of the sequence. Self-attention has been 
            > used successfully in a variety of tasks...
            
            **Source:** `attention_is_all_you_need.pdf` - Page 4
            """)
        
        with st.expander("📄 Result 2 - Transformer Architecture (Score: 82.3%)"):
            st.markdown("""
            **Relevant excerpt:**
            > The Transformer uses multi-head attention in three different ways:
            > In "encoder-decoder attention" layers, the queries come from the previous decoder layer,
            > and the memory keys and values come from the output of the encoder...
            
            **Source:** `attention_is_all_you_need.pdf` - Page 5
            """)

# Sidebar
with st.sidebar:
    st.markdown("## 🛠️ Project Details")
    st.markdown("""
    **Technologies Used:**
    - 🦜 LangChain
    - 🗄️ ChromaDB
    - 🚀 FastAPI
    - 🤗 Sentence Transformers
    - 📊 Streamlit
    
    **Architecture:**
    1. Document ingestion & chunking
    2. Embedding generation
    3. Vector storage & indexing
    4. Semantic similarity search
    5. Result ranking & display
    """)
    
    st.markdown("---")
    st.markdown("### 📌 Links")
    st.markdown("- [GitHub Repository](https://github.com/MrKunalSharma/rag-document-qa)")
    st.markdown("- [Full Documentation](https://github.com/MrKunalSharma/rag-document-qa#readme)")
    
    st.markdown("---")
    st.info("**Note:** This is a demonstration interface. For full functionality with actual document processing, please clone and run the complete system locally.")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Documents Processed", "3", "PDF files")
with col2:
    st.metric("Total Chunks", "400+", "searchable segments")
with col3:
    st.metric("Avg Response Time", "<1s", "per query")

st.caption("Built with ❤️ by Kunal Sharma • RAG Document Q&A System")
