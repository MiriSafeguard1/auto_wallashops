from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def open_product_page(self):
        # Wait for the page to load completely
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"homepage\"]")))
        
        # Click on a product
        link = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"homepage\"]/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[1]/a")))
        print(link.get_attribute("href"))
        self.driver.get(link.get_attribute("href"))

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='main']/div[3]/div[2]/div[2]/div[4]/div[3]/div[4]/div[2]/div[4]/div/div/button[2]/span")))
        add_to_cart_button.click()

    # def open_cart_from_product_page(self):
        # wait = WebDriverWait(self.driver, 5)
        # cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'לצפייה בסל (4)')]")))
        # cart_button.click()