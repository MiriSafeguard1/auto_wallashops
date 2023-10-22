from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.CART_URL = "https://www.wallashops.co.il/cart"

    def close_popup(self):
            try:
                wait = WebDriverWait(self.driver, 5)
                close_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/button/svg/path")))
                close_button.click()
            except:
                pass
            
    def open_product_page(self):
        # Wait for the page to load completely
        wait = WebDriverWait(self.driver, 5)
        ProductPage.close_popup(self.driver)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"homepage\"]")))
        # Click on a product
        link = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"homepage\"]/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[1]/a")))
        self.driver.get(link.get_attribute("href"))
        return True

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        ProductPage.close_popup(self.driver)
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"main\"]/div[3]/div[2]/div[2]/div[4]/div[3]/div[4]/div[2]/div[4]/div/div/button[1]")))
        add_to_cart_button.click()
        return True

    def open_cart_from_product_page(self):
        ProductPage.close_popup(self.driver)
        self.driver.get(self.CART_URL)
        return True

    def verify_product_added_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        ProductPage.close_popup(self.driver)
        cart_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/div/h1/span[2]')))
        return cart_div.text != "0"

   

