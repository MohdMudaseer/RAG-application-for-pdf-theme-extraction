from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import io

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        file_bytes = pdf_file.read()
        reader = PdfReader(io.BytesIO(file_bytes))
        for page_num, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                images = convert_from_bytes(file_bytes, first_page=page_num, last_page=page_num)
                for img in images:
                    text += pytesseract.image_to_string(img)
    except Exception as e:
        print(f"[OCR Fallback] Error: {e}")
        text = ocr_from_image(file_bytes)
    return text

def ocr_from_image(file_bytes):
    pages = convert_from_bytes(file_bytes)
    return ''.join(pytesseract.image_to_string(img) for img in pages)
