import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from sklearn.metrics.pairwise import cosine_similarity

# Load API Key from Streamlit Secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI model & parser
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
parser = StrOutputParser()

# Streamlit UI
st.title("📄 Chat with Your PDF")
st.write("Upload a PDF and ask questions based on its content.")

# File upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Save uploaded file temporarily
    pdf_path = "uploaded_document.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load and process PDF
    loader = PyMuPDFLoader(pdf_path)
    text_documents = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    documents = text_splitter.split_documents(text_documents)

    # Generate embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    doc_embeddings = [embeddings.embed_query(doc.page_content) for doc in documents]

    # User input
    user_query = st.text_input("Ask a question about the document:")

    if user_query:
        # Embed user query
        embedded_query = embeddings.embed_query(user_query)

        # Compute cosine similarity
        similarities = [cosine_similarity([embedded_query], [doc_emb])[0][0] for doc_emb in doc_embeddings]

        # Retrieve most relevant chunk
        best_match_index = similarities.index(max(similarities))
        context = documents[best_match_index].page_content

        # Define and invoke prompt
        template = """
        Answer the question based on the context below. If you can't answer, reply "I don't know".

        Context: {context}

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model | parser
        response = chain.invoke({"context": context, "question": user_query})

        # Display answer
        st.write("### 📝 Answer:")
        st.success(response)
