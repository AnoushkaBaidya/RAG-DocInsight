import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_community.vectorstores import FAISS

def load_pdf_content(file_path):
    """
    Extract content from a PDF file using PDFPlumberLoader.

    Args:
    file_path (str): The file path of the PDF.

    Returns:
    list: A list of Document objects containing the extracted content.
    """
    pdf_loader = PDFPlumberLoader(file_path)
    return pdf_loader.load()

def divide_text_into_chunks(documents, chunk_size=500, chunk_overlap=100):
    """
    Break down documents into smaller text chunks for efficient processing.

    Args:
    documents (list): The list of Document objects to process.
    chunk_size (int): Number of characters per chunk.
    chunk_overlap (int): Number of overlapping characters between chunks.

    Returns:
    list: A list of chunked Document objects.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

def build_vector_store(documents, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Generate a FAISS vector store from documents using HuggingFace embeddings.

    Args:
    documents (list): Documents to be embedded into the vector store.
    model_name (str): HuggingFace model to use for generating embeddings.

    Returns:
    FAISS: A FAISS vector store containing the embedded documents.
    """
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    return FAISS.from_documents(documents, embedding_model)

def get_relevant_documents(vector_store, query, k=3):
    """
    Fetch the top k relevant documents from the FAISS vector store based on a query.

    Args:
    vector_store (FAISS): The FAISS vector store to search.
    query (str): The search query.
    k (int): The number of top relevant documents to retrieve.

    Returns:
    list: A list of the most relevant Document objects.
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)

def save_uploaded_file(uploaded_file):
    """
    Temporarily save an uploaded file to disk.

    Args:
    uploaded_file (UploadedFile): File uploaded through Streamlit or similar interface.

    Returns:
    str: Path to the saved temporary file.
    """
    temp_path = "temp.pdf"
    with open(temp_path, "wb") as file:
        file.write(uploaded_file.getvalue())
    return temp_path

def delete_temp_file(file_path):
    """
    Remove the temporary file from the disk.

    Args:
    file_path (str): The path of the temporary file to delete.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
