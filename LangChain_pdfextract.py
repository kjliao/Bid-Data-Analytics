#https://python.langchain.com/docs/concepts/tools/

from langchain_core.tools import tool
import pandas as pd
import fitz  # PyMuPDF


@tool
def pdfextract(pdf_path, keywords): 
    """Extract sentences containing specific keywords from a PDF file.""" 

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")

        # Split the text into sentences based on periods followed by a space, colons, and bullet points
        sentences = text.split('. ')

        # Extract sentences containing the word "breast" and excluding those containing "www" and "Table of Contents"
        for sentence in sentences:
            if keywords in sentence.lower() and "www" not in sentence.lower() and "table of contents" not in sentence.lower():
                sentences.append((page_num + 1, sentence.strip()))

    return sentences
   
result = pdfextract.invoke({"pdf_path":"xxx", "keywords":"yyy"})
print(result)