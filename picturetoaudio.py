from gtts import gTTS
import os
import pytesseract
img = input("Location of the image:")
text = pytesseract.image_to_string(img)
print(text)
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
