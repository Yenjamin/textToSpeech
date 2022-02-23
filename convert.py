from email import message
from email.message import Message
from gtts import gTTS
from playsound import playsound
import os

def convert(words):
    toConvert = words.get()
    if toConvert != "":
        speech = gTTS(text=toConvert)
        speech.save("converted.mp3")
        playsound("converted.mp3")
        os.remove("converted.mp3")