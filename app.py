import tempfile
import streamlit as st

from rag_pipeline import ScientificRAG


st.set_page_config(
    page_title="Scientific Paper Copilot",
    page_icon="📄",
    layout="wide"
)

st.title("Scientific Research Copilot")
st.caption("Chat with scientific papers, equations and methodologies")


# ---------- Session State ----------

if "rag" not in st.session_state:
    st.session_state.rag = ScientificRAG()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "paper_processed" not in st.session_state:
    st.session_state.paper_processed = False

if "uploaded_filename" not in st.session_state:
    st.session_state.uploaded_filename = None


# ---------- Sidebar ----------

with st.sidebar:

    st.header("Upload Research Paper")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    # Process only new files
    if uploaded_file and uploaded_file.name != st.session_state.uploaded_filename:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        with st.spinner("Processing paper..."):

            try:
                st.session_state.rag.process_pdf(pdf_path)

                st.session_state.paper_processed = True
                st.session_state.uploaded_filename = uploaded_file.name
                st.session_state.messages = []

                st.success("Paper processed successfully")

            except Exception as e:
                st.error(f"Failed to process paper: {e}")

    st.divider()

    st.subheader("Try asking")

    st.markdown("""
    - Explain equation 4  
    - Summarize methodology  
    - Why is this PDE used?  
    - What assumptions are made?  
    - How would I implement this?
    """)

    st.divider()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------- Chat History ----------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------- User Input ----------

user_question = st.chat_input("Ask about the paper...")

if user_question:

    if not st.session_state.paper_processed:
        st.warning("Please upload a research paper first.")
        st.stop()

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = st.session_state.rag.ask_question(user_question)

            except Exception:
                response = (
                    "Model temporarily unavailable or token limit exceeded. "
                    "Please wait a minute and try again."
                )

        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

