import pytesseract
import platform
import os

def configure_tesseract():
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
                return True
    return False

# Run configuration on import
configure_tesseract()
