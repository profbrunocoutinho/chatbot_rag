import streamlit as st
import torch
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# Detectar GPU
device = 0 if torch.cuda.is_available() else -1

# Carregar modelo
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-large",
    max_length=512,
    device=device
)
llm = HuggingFacePipeline(pipeline=qa_pipeline)

# Carregar base FAISS
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={"k": 2})

# Criar cadeia RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

# Streamlit UI
st.set_page_config(page_title="Chatbot RAG com PDFs", layout="centered")
st.title("📘 Chatbot RAG com PDFs")
st.write("Faça uma pergunta com base nos documentos carregados.")

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Perguntar"):
    if pergunta.strip():
        with st.spinner("Consultando..."):
            resposta = qa_chain.run(pergunta)
            st.success(resposta)
    else:
        st.warning("Digite uma pergunta válida.")
