# 📄 Chat with PDFs

## 📝 Overview

This is a **Streamlit-based** application that allows users to **upload a PDF** and ask questions about its content using **OpenAI's GPT model**. The app extracts text from the PDF, generates embeddings, and retrieves the most relevant information to answer user queries.

## 🚀 Features

- 📂 Upload and process **PDF documents**
- 🔍 Use **AI-powered search** to extract relevant information
- 💬 Chat with the document using **GPT-3.5-turbo**
- 🔒 Secure API key handling using **Streamlit Secrets**

## 🛠️ Installation

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/Hisham1799/Chat_with_PDFs.git
cd Chat_with_PDFs
```

### **2️⃣ Create a Virtual Environment (Recommended)**

```sh
python -m venv .venv  # Create virtual environment
source .venv/bin/activate  # On Mac/Linux
.venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Add OpenAI API Key**

#### **For Local Testing**

Create a `.env` file in the root directory and add:

```sh
OPENAI_API_KEY=your-openai-api-key-here
```

#### **For Deployment on Streamlit**

Go to **Streamlit Cloud → Manage App → Secrets** and add:

```sh
OPENAI_API_KEY="your-secret-key-here"
```

## 🎮 Usage

### **Try it Online**
Check out the live version of the app here: [Chat with PDFs](https://hisham1799-chat-with-pdfs-app-voxy3y.streamlit.app/)

### **Run Locally**

```sh
streamlit run app.py
```

### **Deploy on Streamlit Cloud**

1. **Push to GitHub**

```sh
git add .
git commit -m "Initial commit"
git push origin main
```

2. \*\*Go to \*\***[Streamlit Community Cloud](https://streamlit.io/cloud)** and deploy your app.

## 🏗️ Project Structure

```
Chat_with_PDFs/
│── app.py                # Main Streamlit app
│── requirements.txt       # Dependencies
│── .gitignore             # Ignore sensitive files
│── .env (ignored)         # API key (Local use only)
│── README.md              # Project documentation
```

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - UI Framework
- [LangChain](https://python.langchain.com/) - AI Processing
- [OpenAI GPT-3.5](https://openai.com/) - AI Model
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF Processing

## 📜 License

This project is **MIT licensed**.

## 📩 Contact

For any issues or suggestions, feel free to open an **issue** or reach out to **Hisham1799** on GitHub.

---

Enjoy chatting with your PDFs! 🚀

