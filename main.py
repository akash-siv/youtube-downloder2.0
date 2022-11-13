import time
from selinium_script import video_list, download

time.sleep(3)
link_list = list(video_list())
print(len(link_list))
print(link_list)

for i in link_list:
    length = len(i)
    download(i)

# Todo: check the whach later if it is already unticked, if it is already unticked leave it.
# Todo: implement driver.quit().
