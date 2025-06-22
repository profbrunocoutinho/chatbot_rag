# 🦙 Chatbot RAG com LLaMA (Execução Local)

Este projeto é um chatbot orquestrador do tipo **RAG (Retrieval-Augmented Generation)** utilizando o modelo **LLaMA ou Mistral quantizado (.gguf)** para execução local com `llama-cpp-python`.

O chatbot permite consultas semânticas a documentos PDF indexados via FAISS, com interface web desenvolvida em **Streamlit**.

---

## ✅ Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- LangChain
- FAISS (persistência vetorial)
- Hugging Face Embeddings (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`)
- `llama-cpp-python` (modelo local quantizado)
- Modelos suportados: LLaMA, Mistral ou compatíveis no formato `.gguf`

---

## ⚙️ Pré-Requisitos

- Python 3.10 ou superior instalado
- Compilador C/C++ configurado (Visual Studio Build Tools no Windows)
- CMake instalado
- `llama-cpp-python` corretamente instalado (compilado)
- Arquivo `.gguf` do modelo LLaMA ou Mistral baixado
- Base FAISS previamente criada com os documentos PDF

---

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/chatbot-rag-llama.git
cd chatbot-rag-llama

