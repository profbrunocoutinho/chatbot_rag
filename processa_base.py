import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Caminho da pasta com os PDFs
pasta_pdfs = "documentos"

# Carregar todos os PDFs
documentos = []
for nome_arquivo in os.listdir(pasta_pdfs):
    if nome_arquivo.lower().endswith(".pdf"):
        caminho = os.path.join(pasta_pdfs, nome_arquivo)
        loader = PyMuPDFLoader(caminho)
        docs = loader.load()
        documentos.extend(docs)

# Quebrar em pedaços menores para melhor recuperação
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
split_docs = splitter.split_documents(documentos)

# Criar embeddings com modelo multilíngue compatível com pt-br
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Criar e salvar base vetorial FAISS
db = FAISS.from_documents(split_docs, embedding_model)
os.makedirs("faiss_index", exist_ok=True)
db.save_local("faiss_index")

print("✅ Base FAISS com modelo multilíngue (pt-br) salva com sucesso.")
