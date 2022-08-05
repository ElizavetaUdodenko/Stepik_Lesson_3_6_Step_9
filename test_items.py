from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_btn_exist(browser):
    browser.get(link)
    btn = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert btn is not None, "Button does not exist."

