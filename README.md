# GEMINI_LANGCHAIN_PDF-READER
# 🌟 Chat with Multiple PDFs - Powered by Gemini Pro

This is a **Streamlit-based** application that allows users to upload multiple PDF files and ask questions based on their content. The app utilizes **Google Gemini Pro**, **LangChain**, and **FAISS** for efficient document retrieval and question-answering.

---

## 🎯 Features
- 📤 **Upload Multiple PDFs** and extract text from them.
- 🔍 **Ask questions** related to the content of the PDFs.
- ⚡ **Uses Google Gemini Pro** for answering queries.
- 🧠 **Leverages FAISS** for efficient document search and retrieval.

---

## 📌 Requirements
Ensure you have the following dependencies installed:

```bash
streamlit
google-generativeai
python-dotenv
langchain
PyPDF2
faiss-cpu
langchain_google_genai
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/chat-with-pdfs.git
cd chat-with-pdfs
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Google API Key
Create a `.env` file in the root directory and add your API key:
```plaintext
GOOGLE_API_KEY=your_google_api_key_here
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🎯 How to Use
1️⃣ **Upload one or more PDF files.** 📂
2️⃣ **Type a question** related to the uploaded PDFs. 📝
3️⃣ **Get instant answers** powered by **Google Gemini Pro**! 🚀

---

## ❓ Troubleshooting
❌ **Google API Key Not Found?** Ensure your API key is set correctly in the `.env` file.

❌ **Text Extraction Fails?** Try uploading a different PDF file.

❌ **Missing Dependencies?** Run:
```bash
pip install -r requirements.txt
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

💡 *Feel free to contribute or suggest improvements!* 😃
