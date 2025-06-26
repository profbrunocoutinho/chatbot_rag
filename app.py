import streamlit as st
import torch
from langchain_community.llms import LlamaCpp
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Verificar GPU
device = "GPU disponível" if torch.cuda.is_available() else "Usando CPU"

# Caminho para o modelo LLaMA local (substitua pelo seu arquivo)
caminho_modelo = "./modelos/mistral-7b-instruct-v0.2.Q5_K_M.gguf"

# Carregar modelo LLaMA
llm = LlamaCpp(
    model_path=caminho_modelo,
    temperature=0.2,
    max_tokens=512,
    top_p=0.9,
    verbose=True
)

# Carregar o índice FAISS
db = FAISS.load_local(
    "faiss_index", 
    HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    allow_dangerous_deserialization=True
    )

retriever = db.as_retriever(search_kwargs={"k": 3})  # Buscar 3 trechos relevantes

# Interface Streamlit
st.title("Chatbot RAG com Fontes")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    with st.spinner("Buscando resposta..."):
        # Etapa 1: Recuperar os documentos
        documentos = retriever.get_relevant_documents(pergunta)

        # Montar o contexto com os trechos recuperados
        contexto = "\n\n".join([doc.page_content for doc in documentos])

        # Etapa 2: Criar o prompt com contexto + pergunta
        prompt = f"Contexto:\n{contexto}\n\nPergunta: {pergunta}\n\nResposta:"

        # Etapa 3: Gerar a resposta
        resposta = llm(prompt)

        # Exibir a resposta
        st.write("### Resposta:")
        st.write(resposta)

        # Exibir os trechos utilizados
        with st.expander("🔍 Mostrar trechos utilizados na resposta"):
            for i, doc in enumerate(documentos):
                st.write(f"**Trecho {i+1}:** {doc.page_content}")
                if 'source' in doc.metadata:
                    st.write(f"_Fonte:_ {doc.metadata['source']}")
                st.write("---")