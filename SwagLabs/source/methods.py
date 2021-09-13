from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import time


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
    message = ""
    if identifier == "id":
        try:
            element = driver.find_element(By.ID, value)
        except Exception:
            message = "Element not found"
    elif identifier == "class":
        try:
            element = driver.find_element(By.CLASS_NAME, value)
        except Exception:
            message = "Element not found"
    elif identifier == "name":
        try:
            element = driver.find_element(By.NAME, value)
        except Exception:
            message = "Element not found"
    elif identifier == "xpath":
        try:
            element = driver.find_element(By.XPATH, value)
        except Exception:
            message = "Element not found"
    elif identifier == "tag_name":
        try:
            element = driver.find_element(By.TAG_NAME, value)
        except Exception:
            message = "Element not found"
    elif identifier == "css_selector":
        try:
            element = driver.find_element(By.CSS_SELECTOR, value)
        except Exception:
            message = "Element not found"
    elif identifier == "link_text":
        try:
            element = driver.find_element(By.LINK_TEXT, value)
        except Exception:
            message = "Element not found"
    elif identifier == "partial_link_text":
        try:
            element = driver.find_element(By.PARTIAL_LINK_TEXT, value)
        except Exception:
            message = "Element not found"

    return {"element": element, "message": message}


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
            if(driver.find_element_by_link_text(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "partial_link_text":
        try:
            if(driver.find_element_by_partial_link_text(value)):
                return True
            else:
                return False
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


def verify_elements_present(driver, identifier, value):
    if identifier == "id":
        try:
            if(driver.find_elements_by_id(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "name":
        try:
            if(driver.find_elements_by_name(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "xpath":
        try:
            if(driver.find_elements_by_xpath(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "link_text":
        try:
            if(driver.find_elements_by_link_text(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "partial_link_text":
        try:
            if(driver.find_elements_by_partial_link_text(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "tag_name":
        try:
            if(driver.find_elements_by_tag_name(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "class":
        try:
            if(driver.find_elements_by_class_name(value)):
                return True
            else:
                return False
        except:
            return False

    elif identifier == "css_selector":
        try:
            if(driver.find_elements_by_css_selector(value)):
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


def add_to_shopping_cart(driver, product_name="Sauce Labs Bike Light"):
    added = False
    message = ""

    if item_in_cart(driver, product_name):
        added = False
        message = "Item already in cart"

        return {"added": added, "message": message}

    product_names = driver.find_elements(
        By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item']/div[@class='inventory_item_description']/div[@class='inventory_item_label']/a/div")

    count = 1
    for name in product_names:
        if name.text == product_name:
            driver.find_element(
                By.XPATH, "//div[@class='inventory_list']/div[{}]/div[@class='inventory_item_description']/div[@class='pricebar']/button".format(count)).click()
            break
        count = count + 1

    if item_in_cart(driver, product_name):
        added = True
        return {"added": added, "message": message}
    else:
        added = False
        message = "The item was not added to cart"
        return {"added": added, "message": message}


def remove_from_cart(driver, product_name):
    removed = False
    message = ""

    view_cart(driver)
    time.sleep(1)

    if item_in_cart(driver, product_name):

        shopping_cart_items = driver.find_elements(
            By.XPATH, "//div[@class='cart_list']/div/div[@class='cart_item_label']/a/div[@class='inventory_item_name']")

        position = 3
        for item in shopping_cart_items:
            if item.text == product_name:
                driver.find_element(
                    By.XPATH, "//div[@class='cart_list']/div[{}]/div[@class='cart_item_label']/div[@class='item_pricebar']/button".format(position)).click()
                removed = True
            position = position + 1

        if item_in_cart(driver, product_name):
            message = "Item still in cart."
            return {"removed": removed, "message": message}

    else:
        message = "Item not in cart."

    return {"removed": removed, "message": message}


def item_in_cart(driver, item_name):
    view_cart(driver)

    shopping_cart_items = driver.find_elements(
        By.XPATH, "//div[@class='cart_list']/div/div[@class='cart_item_label']/a/div[@class='inventory_item_name']")

    for item in shopping_cart_items:
        if item.text == item_name:
            return True

    driver.find_element(By.ID, "continue-shopping").click()

    return False


def view_cart(driver):
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()


def checkout(driver):
    pass
