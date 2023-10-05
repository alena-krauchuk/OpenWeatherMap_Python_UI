import json
import os
import shutil

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from locators.sign_in_page_locators import SingInPageLocators as sil
from locators.header_page_locators import HeaderPageLocators as hpl
from data.data_urls import MAIN_PAGE_URL
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


@pytest.fixture(scope="session")
def config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "config.json")
    with open(config_file) as f:
        config = json.load(f)
    return config
