# ocr.py

from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='pol')
        return text
    except Exception as e:
        return f"Błąd podczas przetwarzania obrazu: {e}"

if __name__ == "__main__":
    image_path = "opencv_basic/images/image4.png" 
    extracted_text = extract_text_from_image(image_path)
    print("Wydobyty tekst:")
    print(extracted_text)