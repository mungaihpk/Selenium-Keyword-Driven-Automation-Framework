from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


def open_browser(browser_choice):
    driver = None

    if browser_choice == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_choice == "Firefox":
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
    if browser_choice == "Chromium":
        driver = webdriver.Chrome(ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install())
    if browser_choice == "IE":
        driver = webdriver.Ie(IEDriverManager().install())
    if browser_choice == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    if browser_choice == "Opera":
        driver = webdriver.Opera(
            executable_path=OperaDriverManager().install())

    return driver


def get_web_element(driver, identifier, value):
    if identifier == "id":
        element = driver.find_element(By.ID, value)
    elif identifier == "class":
        element = driver.find_element(By.CLASS_NAME, value)
    elif identifier == "name":
        element = driver.find_element(By.NAME, value)
    elif identifier == "xpath":
        element = driver.find_element(By.XPATH, value)
    elif identifier == "tag_name":
        element = driver.find_element(By.TAG_NAME, value)
    elif identifier == "css_selector":
        element = driver.find_element(By.CSS_SELECTOR, value)
    elif identifier == "link_text":
        element = driver.find_element(By.LINK_TEXT, value)
    elif identifier == "partial_link_text":
        element = driver.find_element(By.PARTIAL_LINK_TEXT, value)

    return element


def verify_text_present(driver, text):
    pass


def verify_element_present(driver, identifier, value):
    if identifier == "id":
        try:
            if(driver.find_element_by_id(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "name":
        try:
            if(driver.find_element_by_name(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "xpath":
        try:
            if(driver.find_element_by_xpath(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "link_text":
        try:
            element = driver.find_element(By.LINK_TEXT, value)
            return True
        except:
            return False

    elif identifier == "partial_link_text":
        try:
            element = driver.find_element(By.PARTIAL_LINK_TEXT, value)
            return True
        except:
            return False

    elif identifier == "tag_name":
        try:
            if(driver.find_element_by_tag_name(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "class":
        try:
            if(driver.find_element_by_class_name(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "css_selector":
        try:
            if(driver.find_element_by_css_selector(value)):
                return True
            else:
                return False
        except:
            return False


def input_data(driver, element, text):
    element.send_keys(text)


def verify_text(driver, element, value):
    pass


def verify_text_contains(driver, element, value):
    pass


def verify_element_visible(driver, element):
    if element.is_displayed():
        return True
    else:
        return False
