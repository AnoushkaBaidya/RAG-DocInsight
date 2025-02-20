import streamlit as st
import ollama
from utils import load_pdf_content, divide_text_into_chunks, build_vector_store, get_relevant_documents, save_uploaded_file, delete_temp_file

# Configure Streamlit Page
st.set_page_config(
    page_title="DocInsight",
    page_icon="📄",
    layout="centered"
)

# Custom Styling for DocInsight Interface
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        body {
            background-color: #1B1F3B;
            color: #ECEFF4;
            font-family: 'Poppins', sans-serif;
        }
        .highlight-box {
            background-color: #283046;
            border-left: 10px solid #5A8DEE;
            padding: 12px;
            margin: 12px 0;
            font-size: 14px;
            font-style: italic;
            color: #C3BAC6;
            border-radius: 5px;
        }
        .main-header {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            color: #5A8DEE;
            margin-top: 20px;
        }
        .sub-header {
            text-align: center;
            font-size: 18px;
            color: #B0BEC5;
            margin-bottom: 20px;
        }
        .welcome-message {
            text-align: center;
            font-size: 28px;
            font-weight: 600;
            color: #5A8DEE;
            margin-top: 40px;
        }
        .footer-text {
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-top: 30px;
        }
        .app-logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 60px;
        }
    </style>
""", unsafe_allow_html=True)

# App Header and Introduction
st.markdown('<div class="welcome-message">Hi, I am DocInsight 📚🔍</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">RAG PDF Assistant: Effortless Document Exploration</div>', unsafe_allow_html=True)

# Initialize Session State Variables
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "📄 Upload a PDF and ask me anything about its content!"}
    ]

# Sidebar for PDF Upload
st.sidebar.header("📂 Upload PDF")
uploaded_file = st.sidebar.file_uploader("Upload your PDF file here", type=["pdf"])

# Process the Uploaded PDF
if uploaded_file:
    temp_file_path = save_uploaded_file(uploaded_file)

    # Extract text from PDF
    pdf_text = load_pdf_content(temp_file_path)

    # Split text into manageable chunks
    document_chunks = divide_text_into_chunks(pdf_text)

    # Create vector embeddings for the chunks
    vector_store = build_vector_store(document_chunks)
    st.session_state.vector_store = vector_store
    st.sidebar.success("✅ PDF uploaded and processed! Ask your questions now.")

    # Delete the temporary file after processing
    delete_temp_file(temp_file_path)

# Display Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "<think>" in message["content"]:
            formatted_msg = message["content"].replace("<think>", '<div class="highlight-box">').replace("</think>", "</div>")
            st.markdown(formatted_msg, unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

# User Input for Querying PDF Content
user_query = st.chat_input("Ask something about your PDF...")

if user_query:
    # Show user query immediately
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Only proceed if the vector store is available
    if st.session_state.vector_store:
        with st.spinner("🧠💭 Analyzing..."):
            relevant_documents = get_relevant_documents(st.session_state.vector_store, user_query)

            if not relevant_documents or not relevant_documents[0].page_content.strip():
                response_text = "⚠️ I couldn't find anything relevant. Try asking a different question."
            else:
                combined_context = "\n".join([doc.page_content for doc in relevant_documents])

                ai_response = ollama.chat(
                    model="deepseek-r1:1.5b",
                    messages=[
                        {"role": "system", "content": "You are an AI assistant helping users explore PDF content. Provide accurate and clear responses based on the uploaded document."},
                        {"role": "user", "content": f"Refer to the following content and answer the question clearly:\n\n---\n{combined_context}\n---\n\nQuestion: {user_query}"}
                    ]
                )
                response_text = ai_response["message"]["content"]

        # Display assistant response
        st.session_state.messages.append({"role": "assistant", "content": response_text})

        with st.chat_message("assistant"):
            if "<think>" in response_text:
                formatted_response = response_text.replace("<think>", '<div class="highlight-box">').replace("</think>", "</div>")
                st.markdown(formatted_response, unsafe_allow_html=True)
            else:
                st.markdown(response_text)
