import re
from dotenv import load_dotenv
from parser import extract_text_from_pdf
from prompts import SYSTEM_PROMPT

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from langchain_classic.memory import ConversationSummaryMemory
from langchain_classic.chains import ConversationalRetrievalChain


load_dotenv()


class ScientificRAG:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )

        self.llm = ChatGroq(
            model="qwen/qwen3-32b",
            temperature=0.2,
            max_tokens=500
        )

        self.memory = ConversationSummaryMemory(
            llm=self.llm,
            memory_key="chat_history",
            return_messages=True
        )

        self.vector_db = None
        self.conversation_chain = None


    def _section_chunk_text(self, text):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            separators=[
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            ". ",
            " "
            ]
        )

        return splitter.split_text(text)



    def process_pdf(self, pdf_path):

        text = extract_text_from_pdf(pdf_path)

        chunks = self._section_chunk_text(text)

        self.vector_db = Chroma.from_texts(
            texts=chunks,
            embedding=self.embedding_model,
            persist_directory="chroma_db"
        )

        retriever = self.vector_db.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 4, "fetch_k": 20}
        )

        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=self.memory,
            verbose=False
        )

    def ask_question(self, question):

        if self.conversation_chain is None:
            return "Upload a paper first."

        prompt = f"""
{SYSTEM_PROMPT}

Question:
{question}

Instructions:

1. Prioritize the uploaded paper.

2. If the paper lacks details, use scientific reasoning and clearly mention it is an inference.

3. Explain equations step-by-step if present.

4. Explain PDEs intuitively and mathematically.

5. Explain symbols and physical meaning.

6. If implementation is asked, provide PyTorch-level logic.

7. Keep responses concise unless detailed explanation is explicitly requested.

8. Structure answers clearly.
"""

        response = self.conversation_chain.invoke({"question": prompt})

        answer = response["answer"]

        if "<think>" in answer:
            answer = re.sub(
            r"<think>.*?</think>",
            "",
            answer,
            flags=re.DOTALL
            ).strip()

