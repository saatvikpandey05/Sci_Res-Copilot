import pymupdf4llm


def extract_text_from_pdf(pdf_path):

    markdown_text = pymupdf4llm.to_markdown(pdf_path)

    cleaned_text = "\n".join(
        line.strip()
        for line in markdown_text.splitlines()
        if line.strip()
    )

    return cleaned_text

