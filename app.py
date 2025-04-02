import os
import streamlit as st
import PyPDF2
import faiss
import tempfile
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.llms import GoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Google Gemini Pro model
def get_llm():
    return GoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# Function to extract text from PDF
def extract_text_from_pdfs(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        with pdf_file as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    return text

# Streamlit UI
st.title("Chat with Multiple PDFs - Gemini Pro")

uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write("Processing files...")
    text_data = extract_text_from_pdfs(uploaded_files)
    
    # Split text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_text(text_data)
    
    # Generate embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    vectorstore = FAISS.from_texts(texts, embeddings)
    retriever = vectorstore.as_retriever()
    
    # Initialize QA chain
    qa_chain = RetrievalQA(llm=get_llm(), retriever=retriever)
    
    # User input
    query = st.text_input("Ask a question about the PDFs")
    if query:
        response = qa_chain.run(query)
        st.write("### Answer:")
        st.write(response)
