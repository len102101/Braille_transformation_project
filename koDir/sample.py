import pytesseract
from gtts import gTTS
import numpy as np
import cv2
from PIL import Image
from itertools import permutations
from googletrans import Translator


pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata" --psm 1 -c preserve_interword_spaces=1' #  
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        ret, bin = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        img = Image.fromarray(bin)
        img.save("resultKo.png")
        
        try:
            txt = pytesseract.image_to_string(img, lang='kor', config=tessdata_dir_config)
            print('kor', txt)
            translator = Translator()
            tr_results = translator.translate(txt, src='ko', dest='fr').text
            print('fr', tr_results)
            print("-----")
            tts = gTTS(text=tr_results, lang="fr")
            tts.save("resultKo.mp3")
        except:
            print("plz retry")
        
cap.release()
cv2.destroyAllWindows()
