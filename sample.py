# import pytesseract
# from gtts import gTTS
# import numpy as np
# import cv2
# from PIL import Image
# from itertools import permutations


# pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata" --psm 1 -c preserve_interword_spaces=1' #  
# cap = cv2.VideoCapture(0)

# # result = pytesseract.image_to_string('./images/sample06.png', lang='kor', config=tessdata_dir_config)
# # print(result)

# # tts = gTTS(text=result, lang="ko")
# # tts.save("result.mp3")




# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)

    
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
#         ret, bin = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#         img = Image.fromarray(bin)
#         img.save("result.png")
        

#         #img = Image.fromarray(frame) # frame으로 넣어도 된다.
#         txt = pytesseract.image_to_string(img, lang='kor', config=tessdata_dir_config)
#         print(txt)
#         print("-"*10)
        
        
# cap.release()
# cv2.destroyAllWindows()

from itertools import permutations

a = list(permutations("(())", 4))
a = sorted(set(a))
for i in a:
    print("".join(i))