from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            extracted = page.extract_text()
            text += extracted if extracted else ocr_from_image(pdf_file)
    except:
        text = ocr_from_image(pdf_file)
    return text

def ocr_from_image(pdf_file):
    pages = convert_from_bytes(pdf_file.read())
    return ''.join(pytesseract.image_to_string(img) for img in pages)
