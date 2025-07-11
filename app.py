import streamlit as st
import sys
import torch
sys.modules['torch.classes'] = None


st.set_page_config(page_title="AI Assistant with RAG", layout="centered")

# 👨‍💻 HEADER
st.markdown("""
    <h1 style='text-align: center;'>🤖 AI Assistant with RAG</h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>
        Your intelligent assistant powered by retrieval-augmented generation
    </p>
""", unsafe_allow_html=True)

# 🧱 FEATURE CARDS
st.markdown("""
<style>
.card-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1.5rem;
    margin-top: 2rem;
}
.card {
    width: 240px;
    background-color: #f8f9fa;
    padding: 1.25rem;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    text-align: center;
}
.card h4 {
    margin-bottom: 0.5rem;
    color: #333;
}
.card p {
    font-size: 14px;
    color: #666;
}
.button-container {
    text-align: center;
    margin-top: 3rem;
}
.stButton>button {
    background-color: #3366ff;
    color: white;
    padding: 0.75rem 2rem;
    font-size: 16px;
    border: none;
    border-radius: 8px;
}
</style>

<div class="card-container">
    <div class="card">
        <h4>AI-Powered Responses</h4>
        <p>Advanced language understanding with contextual awareness</p>
    </div>
    <div class="card">
        <h4>RAG Knowledge Base</h4>
        <p>Retrieval-augmented generation from your documents</p>
    </div>
    <div class="card">
        <h4>Real-time Processing</h4>
        <p>Fast, streaming responses with source citations</p>
    </div>
    <div class="card">
        <h4>Secure & Private</h4>
        <p>Your data remains private and secure</p>
    </div>
</div>

<div class="button-container">
""", unsafe_allow_html=True)

# 👇 Button to Go to Q&A Page
if st.button("Start a New Conversation"):
    st.switch_page("pages\qa_app.py")  # 👈 Will route to actual app (next step)
