from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

password =  "mpn6jPDhZJ9R!"
username =  "amirg.uni12@gmail.com"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://www.wallashops.co.il/login?rurl=8")

# login options button
button = driver.find_element(By.CLASS_NAME, "mobile-login-btn")
if button.get_attribute("aria-expanded") == "false":
    #change state & toggle to true
    button.click()

#insert username & password in the form
driver.find_element(By.NAME, "loginEmail").send_keys(username)
driver.find_element(By.NAME, "loginPassword").send_keys(password)

# click on login button
button = driver.find_element(By.XPATH, "//button[contains(text(), 'כניסה לוואלה!שופס')]")
button.click()

# click on some product
wait = WebDriverWait(driver, 5)  # Wait for up to 10 seconds
link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "b-product-link")))
driver.get(link.get_attribute("href"))

# click on add to cart -> by clicking on the button getting into the cart
wait = WebDriverWait(driver, 5)  # Wait for up to 10 seconds
button = driver.find_element(By.CLASS_NAME, "js-add-to-cart")
button.click() 
print("success")
