from typing import Text
import cv2
from gtts import gTTS
import os
from PIL import Image
import pytesseract
import pyttsx3
img = input("Location of the image:")
text = pytesseract.image_to_string(img)
print(text)
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")


    



