import fitz  # PyMuPDF

doc = "C:\\Users\\RoiMinuit\\Desktop\\Country\\HOA\Austin Ridge HOA.pdf"

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text

pdf_text = extract_text_from_pdf(doc)
