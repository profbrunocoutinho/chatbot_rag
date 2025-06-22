# 🦥 Chatbot RAG com LLaMA (Execução Local)

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
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Baixe um modelo `.gguf` compatível

- Recomendo: [Mistral 7B Instruct GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
- Coloque o modelo baixado na pasta: `./modelos/`

---

## 🗂️ Estrutura do Projeto

```text
chatbot-rag-llama/
├── app.py                # Interface Streamlit
├── processa_base.py      # Processa PDFs e cria a base FAISS
├── faiss_index/          # Base vetorial persistida
├── modelos/              # Pasta onde deve estar o arquivo .gguf
├── requirements.txt      # Dependências
└── README.md
```

---

## 🖥️ Como Executar

### 1. Processar a base de documentos (se ainda não fez)

```bash
python processa_base.py
```

### 2. Rodar o chatbot

```bash
streamlit run app.py
```

### 3. Acesse no navegador

```text
http://localhost:8501
```

---

## ⚙️ Configurações importantes no `app.py`

- Caminho do modelo:

```python
caminho_modelo = r"C:\Users\SeuUsuario\Documents\chatbot-rag-llama\modelos\mistral-7b-instruct-v0.2.Q4_K_M.gguf"
```

- Parâmetros ajustáveis:

```python
temperature=0.7
max_tokens=512
top_p=0.95
n_ctx=2048
```

---

## 📚 Referências

- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [TheBloke Models - Hugging Face](https://huggingface.co/TheBloke)

---

## 🛡️ Licença

Este projeto utiliza modelos de código aberto sob licenças compatíveis (Apache 2.0, MIT ou permissivas).\
O uso de modelos LLaMA da Meta requer aceitação da licença de uso não comercial.

---

## ✉️ Contato

Desenvolvido por Bruno – Projeto educacional para uso no contexto do Ifes.

