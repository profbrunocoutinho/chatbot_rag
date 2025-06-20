# 🧠 Chatbot RAG com PDFs

Um chatbot baseado em **RAG (Retrieval-Augmented Generation)** que responde perguntas a partir de arquivos PDF carregados. Utiliza o modelo `flan-t5-large`, FAISS para busca semântica e interface via **Streamlit**.

---

## 📁 Estrutura do Projeto

```
chatbot_rag_pdf/
│
├── app.py                # Interface web com Streamlit
├── processa_base.py      # Geração e indexação dos PDFs
├── documentos/           # Coloque aqui os PDFs
├── faiss_index/          # Criado automaticamente (base vetorial)
└── requirements.txt      # Dependências do projeto
```

---

## 💡 Tecnologias Utilizadas

- 🧠 [LangChain](https://python.langchain.com/)
- 🔍 [FAISS](https://github.com/facebookresearch/faiss) para busca vetorial
- 📚 [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- 🔤 Modelo: `google/flan-t5-large`
- 📄 Leitura de PDF com `PyMuPDF`
- 🌐 Interface com [Streamlit](https://streamlit.io)

---

## ✅ Requisitos

- Python 3.9 ou superior
- pip

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-rag-pdf.git
cd chatbot-rag-pdf
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Adicione seus arquivos PDF à pasta `documentos/`.

4. Gere a base FAISS:

```bash
python processa_base.py
```

5. Inicie a interface:

```bash
streamlit run app.py
```

---

## 🖥️ Uso

- Acesse [http://localhost:8501](http://localhost:8501)
- Digite uma pergunta relacionada ao conteúdo dos PDFs carregados
- O chatbot responderá com base no que foi encontrado

---

## 📌 Observações

- O modelo `flan-t5-large` funciona bem com perguntas diretas, mas para respostas mais precisas, é recomendável refinar os PDFs e ajustar os parâmetros do chunking e do retriever.
- A base FAISS é persistente (salva em `faiss_index/`), não sendo necessário reindexar toda vez.
- GPU é usada automaticamente se detectada.

---

## 🔒 Segurança

Ao carregar a base FAISS com `allow_dangerous_deserialization=True`, **certifique-se de que o arquivo **``** foi gerado por você**. Nunca carregue índices `.pkl` de fontes desconhecidas.

---

## 🚀 Possíveis melhorias futuras

- Interface com histórico de chat
- Upload de PDFs direto pela interface
- Deploy na nuvem (Streamlit Cloud, Render, etc.)
- Integração com base de dados relacional

---

## 📄 Licença

Este projeto é de livre uso acadêmico. Adapte conforme sua necessidade.

