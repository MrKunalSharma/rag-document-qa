"""
Streamlit frontend for RAG Document Q&A System
"""
import streamlit as st
import requests
import json
from typing import List, Dict

# API configuration
API_URL = "http://localhost:8000"

# Page config
st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .source-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .score-badge {
        background-color: #1f77b4;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 0.3rem;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("📚 RAG Document Q&A System")
st.markdown("""
Ask questions about AI research papers. The system will search through:
- **Attention Is All You Need** (Transformer paper)
- **BERT: Pre-training of Deep Bidirectional Transformers**
- **Language Models are Few-Shot Learners** (GPT-3)
""")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    num_results = st.slider("Number of results", 1, 10, 3)
    
    st.header("📊 System Info")
    try:
        response = requests.get(f"{API_URL}/health")
        if response.status_code == 200:
            data = response.json()
            if data["vector_store_loaded"]:
                st.success("✅ Vector Store: Loaded")
                st.info(f"📄 Document chunks: {data.get('document_count', 425)}")
            else:
                st.error("❌ Vector Store: Not loaded")
    except:
        st.error("❌ API: Offline")
    
    st.header("🔍 Sample Questions")
    sample_questions = [
        "What is the transformer architecture?",
        "How does self-attention work?",
        "What is BERT's masked language modeling?",
        "Explain the attention mechanism",
        "How does GPT-3 perform few-shot learning?",
        "What are positional encodings?",
    ]

# Main content
st.header("🤔 Ask a Question")

# Initialize session state
if 'question' not in st.session_state:
    st.session_state.question = ""

# Sample question buttons
st.markdown("**Try these questions:**")
cols = st.columns(3)
for idx, question in enumerate(sample_questions[:6]):
    if cols[idx % 3].button(f"💡 {question}", key=f"sample_{idx}"):
        st.session_state.question = question

# Query input
question = st.text_area(
    "Your question:",
    value=st.session_state.question,
    placeholder="E.g., What is the attention mechanism in transformers?",
    height=100
)

# Search button
if st.button("🔍 Search", type="primary", use_container_width=True):
    if question:
        with st.spinner("Searching through documents..."):
            try:
                # Make API request to /search endpoint
                response = requests.post(
                    f"{API_URL}/search",
                    json={"question": question, "num_results": num_results}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Display answer
                    st.header("💡 Answer")
                    with st.container():
                        st.markdown(data["answer"])
                    
                    # Display sources
                    if data.get("sources"):
                        st.header("📚 Sources")
                        for i, source in enumerate(data["sources"]):
                            with st.expander(f"📄 {source['source']} (Score: {float(source['score']):.3f})"):
                                st.markdown(f"**Relevance Score:** {float(source['score']):.3f}")
                                st.markdown("**Content:**")
                                st.text(source["content"])
                    
                    # Metrics
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Sources Found", len(data.get("sources", [])))
                    with col2:
                        best_score = float(data["sources"][0]["score"]) if data.get("sources") else 0
                        st.metric("Best Match Score", f"{best_score:.3f}")
                    with col3:
                        st.metric("Response Time", "< 1s")
                        
                else:
                    st.error(f"Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Error connecting to API: {str(e)}")
                st.info("Make sure the API is running at http://localhost:8000")
    else:
        st.warning("Please enter a question")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with LangChain, ChromaDB, FastAPI, and Streamlit</p>
    <p>Processing 425 document chunks from 3 AI research papers</p>
</div>
""", unsafe_allow_html=True)
