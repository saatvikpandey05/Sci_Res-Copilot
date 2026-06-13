# 🔬 Scientific Research Copilot

> A conversational RAG system for scientific papers — ask questions, understand PDEs, and extract research insights in plain language.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-app-red?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)

---

## What it does

Scientific Research Copilot lets you have a multi-turn conversation with any research paper. Upload a PDF and ask it anything — from high-level methodology questions to specific mathematical derivations. It understands context across turns, so follow-up questions work the way they should.

**Built for:** researchers, students, and engineers who need to move faster through dense technical literature.

---

## Features

| Feature | Description |
|---|---|
| 📄 **Section-aware PDF parsing** | Chunks papers by section (intro, methods, results) for more precise retrieval |
| 🔍 **Semantic retrieval** | BGE embeddings + ChromaDB with MMR-based search for high-relevance context |
| 🧠 **Conversational memory** | Multi-turn Q&A with persistent context across the session |
| ➗ **Mathematical reasoning** | Explains PDEs, derivations, and equations in plain language |
| ⚡ **Fast inference** | Groq-hosted LLMs for low-latency responses |
| 🔁 **Implementation guidance** | Translates methodology into code-level understanding |

---

## Tech Stack

```
Python 3.10
├── LangChain          — RAG pipeline and chain orchestration
├── ChromaDB           — Vector store for semantic retrieval
├── HuggingFace (BGE)  — Scientific text embeddings
├── Groq API           — LLM inference (Llama / Mixtral)
├── PyMuPDF4LLM        — PDF parsing and section extraction
└── Streamlit          — Frontend UI
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/saatvikpandey05/Sci_Res-Copilot.git
cd Sci_Res-Copilot
```

### 2. Create environment

```bash
conda create -p venv python=3.10 -y
conda activate ./venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the app

```bash
streamlit run app.py
```

---

## Example Questions

Once you upload a paper, try asking:

```
"What is the governing PDE and what does each term represent?"
"How does this approach differ from standard PINNs?"
"Summarize the experimental methodology in simple terms."
"What assumptions does the model make, and when might they break down?"
"How would I implement the loss function described in Section 3 in PyTorch?"
"What are the key limitations acknowledged by the authors?"
```

---

## Project Structure

```
Sci_Res-Copilot/
├── app.py                  # Streamlit frontend
├── rag_pipeline.py         # RAG chain + retriever logic
├── pdf_parser.py           # Section-aware PDF chunking
├── embeddings.py           # BGE embedding setup
├── memory.py               # Conversational memory management
├── requirements.txt
└── .env                    # API keys (not committed)
```

> **Note:** The project structure above is illustrative — update file names to match your actual repo layout.

---

## How It Works

```
User Query
    │
    ▼
Conversational Memory  ◄──────────────────────┐
    │                                          │
    ▼                                          │
BGE Embedding of Query                         │
    │                                          │
    ▼                                          │
ChromaDB MMR Retrieval                         │
    │                                          │
    ▼                                          │
Section-aware Chunks from PDF                  │
    │                                          │
    ▼                                          │
Groq LLM (Llama / Mixtral)                     │
    │                                          │
    ▼                                          │
Response ──────────────────────────────────────┘
```

---

## Built By

**Saatvik Pandey** — B.Tech, IIT Patna  
[LinkedIn](https://www.linkedin.com/in/saatvik-pandey-4a0919287) · [GitHub](https://github.com/saatvikpandey05)

---

## License

MIT License. See [`LICENSE`](LICENSE) for details.
