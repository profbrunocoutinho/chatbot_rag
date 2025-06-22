import streamlit as st
import torch
from langchain_community.llms import LlamaCpp
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# Verificar GPU
device = "GPU disponível" if torch.cuda.is_available() else "Usando CPU"

# Caminho para o modelo LLaMA local (substitua pelo seu arquivo)
caminho_modelo = "./modelos/mistral-7b-instruct-v0.2.Q5_K_M.gguf"

# Carregar modelo LLaMA
llm = LlamaCpp(
    model_path=caminho_modelo,
    temperature=0.7,
    max_tokens=512,
    top_p=0.95,
    n_ctx=2048,
    verbose=False
)

# Carregar embeddings e base FAISS
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
db = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

# Criar retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# Pipeline RAG simples (sem prompt customizado)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

# Interface Streamlit
st.set_page_config(page_title="Chatbot RAG com LLaMA", layout="centered")
st.title("🦙 Chatbot RAG com LLaMA")
st.write(f"Dispositivo: {device}")

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Perguntar"):
    if pergunta.strip():
        with st.spinner("Buscando resposta nos documentos..."):
            resposta = qa_chain.run(pergunta)
            st.success(resposta)
    else:
        st.warning("Digite uma pergunta válida.")
