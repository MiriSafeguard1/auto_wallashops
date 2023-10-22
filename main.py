from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import constant
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.wallashops.co.il/login?rurl=8")


# Initialize Page Objects
login_page = LoginPage(driver)
product_page = ProductPage(driver)

# Perform Test Steps
login_page.open()
inSite = login_page.login(constant.USERNAME, constant.PASSWORD)

# Navigate to a product page
product_page.open_product_page()

time.sleep(10)

# Add the product to the cart
product_page.add_to_cart()

# Navigate to the cart
product_page.open_cart_from_product_page()

# verify that the product is added to cart
product_page.verify_product_added_to_cart()

print("autometion Passed")

