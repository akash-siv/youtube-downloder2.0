from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--lang=en-us")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8282")
s = Service('C:/Users/akash/PycharmProjects/youtube_downloader/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://www.youtube.com/playlist?list=WL")
time.sleep(2)
link_list = []

def video_list():
    link_object = driver.find_elements_by_tag_name('a')
    old_list= [page.get_attribute('href') for page in link_object]
    for a in old_list:
        try:
            if "watch" in a:
                link_list.append(a)
        except:
            pass
    return set(link_list)


def download(link):
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get("https://savef.net/en48/?ts=1645019911253&url=https%3A%2F%2Fm.youtube.com%2F")
    current_tab = driver.current_window_handle
    url = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".main-form-input")))
    url.clear()
    url.send_keys(link)
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".main-form-submit"))).click()
    try:
        time.sleep(1)
        chwd = driver.window_handles
        for new_window in chwd:
            # switch focus to child window
            if (new_window != current_tab):
                driver.close()

        driver.switch_to.window(current_tab)
        time.sleep(1)
        a = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "tr:nth-child(3) td:nth-child(1) .download-link-popup-js")))
    except:
        pass
    else:
        if a.text == "720":
            a.click()
            time.sleep(5)
            remove_video(link, driver, current_tab)
        elif WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "tr:nth-child(2) td:nth-child(1) .download-link-popup-js"))).text == "720":
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "tr:nth-child(2) td:nth-child(1) .download-link-popup-js"))).click()
            time.sleep(5)
            remove_video(link, driver, current_tab)
            time.sleep(15)


def remove_video(remove, driver, current_tab):
    try:
        time.sleep(1)
        chwd = driver.window_handles
        for new_window in chwd:
            # switch focus to child window
            if (new_window != current_tab):
                driver.close()

        driver.switch_to.window(current_tab)
        time.sleep(1)
    except:
        pass


    time.sleep(1)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(remove)
    time.sleep(2)

    try:
        skip_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#skip-button\:5 .ytp-button"))).click()
    except:
        pass

    save = driver.find_elements(By.CSS_SELECTOR, '.size-default+ .size-default .ytd-button-renderer')
    print(save)
    # print(save.text)
    try:
        for value in save:
            if value.text == "SAVE":
                value.click()
                print("video deleted")
            # else:

    except TypeError:
        if save.text == "SAVE":
            save.click()
    time.sleep(1)
    watch_later = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#checkboxLabel")))

    try:
        for link in watch_later:
            if link.text == "Watch later":
                link.click()
    except TypeError:
        if watch_later.text == "Watch later":
            watch_later.click()





