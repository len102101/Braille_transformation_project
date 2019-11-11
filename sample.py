import pytesseract
from gtts import gTTS

pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

result = pytesseract.image_to_string('./images/sample06.png', lang='kor', config=tessdata_dir_config)
print(result)

tts = gTTS(text=result, lang="ko")
tts.save("result.mp3")
