import os

def open_chrome():
	os.chdir(r'C:\\Program Files\\Google\\Chrome\\Application\\')
	os.system(r'chrome.exe -start-maximized -remote-debugging-port=8282 --user-data-dir="C:\Users\akash\PycharmProjects\Selenium\youtube_downloader2\chrome_data"')
open_chrome()

