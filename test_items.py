from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_btn_exist(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    btn = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert btn, "Button does not exist."

