import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

a = Image.open('./Macro/예배순서.png')
result = pytesseract.image_to_string(a, lang='kor')
print(result)