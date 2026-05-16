import pytesseract
from PIL import Image
import src.loaders.ocr_utils

def load_image(path):
    """
    Extracts text from an image using OCR.
    """
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text
