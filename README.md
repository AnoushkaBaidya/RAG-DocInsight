# 🤖 RAG PDF Explorer: `DeepSeek-R1`, `Ollama`, `Streamlit`, & `FAISS`

![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-0C0D0E?logo=ollama&logoColor=white)
![PDFPlumber](https://img.shields.io/badge/PDFPlumber-FF0000?logo=pdf&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00ADD8?logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD43B?logo=huggingface&logoColor=black)
![FAISS](https://img.shields.io/badge/FAISS-00A98F?logo=faiss&logoColor=white)

---

## 📌 **Introduction**  

The **RAG PDF Explorer** is an AI-powered **Retrieval-Augmented Generation (RAG)** chatbot built for **intelligent PDF navigation and content extraction.** It harnesses multiple technologies to provide fast and accurate results:  

✅ **DeepSeek-R1 (1.5B)** – State-of-the-art language model ensuring **precise responses.**  
✅ **FAISS** – High-performance vector search enabling **quick document retrieval.**  
✅ **Ollama** – Lightweight model host for **smooth and efficient inference.**  
✅ **LangChain** – Versatile AI framework for **complex query management and reasoning.**  
✅ **Streamlit** – Interactive and user-friendly **web interface.**  

### 🎯 **Key Use Cases**  

🔍 **Instantly search** extensive PDF files.  
📄 **Summarize complex documents** like reports, research articles, and agreements.  
📘 **Extract essential information** with AI-backed precision.  
🤖 **Ask natural language questions** and receive clear, concise answers.  

---

## 📌  **Installation & Setup**  

### **Prerequisites**  

Ensure you have the following installed:  

- **Python 3.9+**  
- **pip** (Python package manager)  
- **Git** (for cloning the repository)  

### **Step 1: Clone the Repository**  

```bash
$ git clone AnoushkaBaidya/RAG-DocInsight
$ cd RAG-DocInsight
```

### **Step 2: Install Dependencies**  

```bash
$ pip install -r requirements.txt
```

### **Step 3: Launch the Application**  

1. Start Ollama service:

   ```bash
   ollama serve
   ```

2. In a new terminal, run the Streamlit app:

   ```bash
   streamlit run app/app.py
   ```

---

## 📌  **How It Operates**  

1️⃣ **Upload a PDF** → The AI scans and organizes the content for analysis.  
2️⃣ **Submit a Query** → The system locates the most relevant sections.  
3️⃣ **Receive an AI-Generated Answer** → Based on the extracted document data.  

🔹 **FAISS** is utilized for **rapid and accurate document searches.**  
🔹 **DeepSeek-R1** delivers **context-aware, high-quality responses.**  

---

## 📌  **Tech Stack Overview**  

| **Technology**     | **Functionality**                        |
|--------------------|------------------------------------------|
| **DeepSeek-R1 (1.5B)** | Advanced language model for insightful answers |
| **Ollama**         | Lightweight model hosting and inference  |
| **FAISS**          | Efficient vector-based document retrieval |
| **LangChain**      | AI-powered reasoning and query management |
| **Streamlit**      | Interactive and user-friendly web interface |
| **PDFPlumber**     | Extracting structured text from PDFs      |

---

### **📌 UI Preview**  
<img width="1263" alt="Screenshot 2025-02-20 at 11 11 28 AM" src="https://github.com/user-attachments/assets/9ca23751-0334-4f9a-9bf5-6d243d2a9e4e" />


