from selenium import webdriver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import constant
import time

def test_wallashops():
    # create a new Chrome browser instance
    driver = webdriver.Chrome()
    driver.maximize_window()

    # create a new LoginPage instance
    login_page = LoginPage(driver)

    # open the login page
    login_page.open()

    # login with valid credentials
    assert login_page.login(constant.USERNAME, constant.PASSWORD)
    print("Login Passed")

    # wait for 2 seconds for the page to load
    time.sleep(2)

    # create a new ProductPage instance
    product_page = ProductPage(driver)

    # open the product page
    assert product_page.open_product_page()
   
    # add product to cart
    assert product_page.add_to_cart()
    print("Add to cart Passed")

    # verify that the product page is displayed
    assert product_page.open_cart_from_product_page()

    # verify that the product is added to cart
    assert product_page.verify_product_added_to_cart()

   # quit the browser
    driver.quit()

    
