from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import constant

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Initialize Page Objects
login_page = LoginPage(driver)
product_page = ProductPage(driver)

# Perform Test Steps
login_page.open()
inSite = login_page.login(constant.USERNAME, constant.PASSWORD)

# Navigate to a product page
# if(inSite):
product_page.open_product_page()

# Add the product to the cart
product_page.add_to_cart()

# Navigate to the cart
# product_page.open_cart_from_product_page()
