from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyautogui
import time


def save(file_name):
    """
    save and rename img.
    """
    pyautogui.write('v')
    time.sleep(0.3)
    pyautogui.press(list(file_name), interval=0.3)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.press('enter')


def perform_img(url):
    """
    infinite loop to download if url exists.
    """
    driver = webdriver.Firefox()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    while True:
        image = wait.until(EC.element_to_be_clickable(("xpath", \
            '//div/div/div/div/img[not (@style="display: none;")]')))
        vol = driver.find_element(By.XPATH, "//div[@class='reader--meta chapter']").text
        actions = ActionChains(driver)
        actions.context_click(image).perform()

        l = driver.current_url.split('/')
        file_name = vol + '-' + l[-1] + '.jpg'
        time.sleep(0.2)
        save(file_name)
        actions.move_to_element_with_offset(image, 300, 0).click().perform()
    

if __name__ == '__main__':
    dir_path = r'C:\Manga'
    # start reading url like: 'https://mangadex.org/chapter/3660abf5-7b72-4a58-954a-c94d31652c08/1'
    base_url = ''
    perform_img(base_url)
    