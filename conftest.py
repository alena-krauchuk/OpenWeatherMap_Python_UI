import json
import os
import shutil

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from data.data_urls import url_main_page
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        driver.set_window_size(1900, 1000)
    else:
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=ChromeService())
        driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait

