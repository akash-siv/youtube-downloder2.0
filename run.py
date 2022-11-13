import os
from subprocess import *
import time

p = Popen([r'C:\Users\akash\PycharmProjects\youtube_downloader\open_chrome.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print (output[0])

time.sleep(3)

p = Popen([r'C:\Users\akash\PycharmProjects\youtube_downloader\main.py', "ArcEditor"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print (output[0])