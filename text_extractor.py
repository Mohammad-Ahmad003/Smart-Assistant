import fitz
def extract_pdf_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def extract_txt_text(file):
    return file.read().decode("utf-8")
