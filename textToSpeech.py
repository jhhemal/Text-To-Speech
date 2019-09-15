# !/usr/bin/env python3
# textToSpeach.py - A python program that will tranfrom text to speach.
# Author - Jahidul Hasan Hemal

from gtts import gTTS
import os
import subprocess, sys
fh = open("text.txt", "r")
myText = fh.read().replace("\n", " ")

language = 'en'
output = gTTS(text=myText, lang=language, slow = False)
output.save("output.mp3")
fh.close()
opener = "open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, "output.mp3"])