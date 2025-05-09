'''
This is an AI Agent that 
1) counts how many pdf files in the folder, 
2) extracts specific information based on certain keywords, and 
3) saves results in an excel file  
'''
from langchain_core.tools import tool
import pandas as pd
import fitz  # PyMuPDF
import os

@tool
def list_files(directory_path):
    """List all files in a directory and return their count and names."""
    try:
        files = os.listdir(directory_path)
        file_count = len(files)
        return {
            "total_files": file_count,
            "file_names": files
        }
    except Exception as e:
        return f"Error accessing directory: {str(e)}"

@tool
def pdfextract(pdf_path, keywords): 
    """Extract sentences containing specific keywords from a PDF file and save to Excel.""" 
    extracted_sentences = []
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")

        # Split the text into sentences based on periods followed by a space, colons, and bullet points
        sentences = text.split('. ')

        # Extract sentences containing the keyword and excluding those containing "www" and "Table of Contents"
        for sentence in sentences:
            if keywords in sentence.lower() and "www" not in sentence.lower() and "table of contents" not in sentence.lower():
                extracted_sentences.append({
                    'Page': page_num + 1,
                    'Sentence': sentence.strip()
                })

    # Create DataFrame and save to Excel
    if extracted_sentences:
        df = pd.DataFrame(extracted_sentences)
        excel_filename = f"extracted_sentences_{os.path.basename(pdf_path).replace('.pdf', '')}.xlsx"
        df.to_excel(excel_filename, index=False)
        return f"Extracted {len(extracted_sentences)} sentences and saved to {excel_filename}"
    else:
        return "No matching sentences found."

dir = input("Directory Path: ")
keyword = input("Keyword for searching: ")

file = list_files.invoke({"directory_path":dir})  
result = pdfextract.invoke({"pdf_path":dir, "keywords":keyword})
print(file)
print(result)
