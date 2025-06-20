# Rode esse script apenas 1 vez sempre que mudar os PDFs.

import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Caminho da pasta com os PDFs
pasta_pdfs = "documentos"

# Carregar todos os PDFs
all_docs = []
for nome_arquivo in os.listdir(pasta_pdfs):
    if nome_arquivo.lower().endswith(".pdf"):
        caminho = os.path.join(pasta_pdfs, nome_arquivo)
        loader = PyMuPDFLoader(caminho)
        docs = loader.load()
        all_docs.extend(docs)

# Quebrar em pedaços
splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
split_docs = splitter.split_documents(all_docs)

# Criar embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Criar base FAISS
db = FAISS.from_documents(split_docs, embedding_model)

# Salvar
os.makedirs("faiss_index", exist_ok=True)
db.save_local("faiss_index")
print("Base FAISS salva com sucesso.")
