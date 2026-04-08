from pypdf import PdfReader
import pytesseract
import fitz  # PyMuPDF
from PIL import Image
import io
import platform
import os

# If on Windows, set tesseract path explicitly if it exists in the default location
if platform.system() == "Windows":
    window_tesseract_paths = [
        r"D:\TESSERACT\tesseract.exe",
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"C:\Users\ASUS\AppData\Local\Tesseract-OCR\tesseract.exe"
    ]
    for ts_path in window_tesseract_paths:
        if os.path.exists(ts_path):
            pytesseract.pytesseract.tesseract_cmd = ts_path
            break

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
            
    # If standard extractions yield no text, we assume it's a scanned PDF and attempt OCR
    if not text.strip():
        text = ""
        pdf_document = fitz.open(path)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(dpi=300)
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Run OCR
            ocr_text = pytesseract.image_to_string(img)
            text += ocr_text + "\n"
            
    return text