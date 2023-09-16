from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://www.wallashops.co.il/login?rurl=8")
password =  "mpn6jPDhZJ9R!"
username =  "amirg.uni12@gmail.com"
driver.find_element_by_class_name("mobile-login-btn f-button f-button--white f-button--full-width collapsed").click()
# driver.find_element_by_id("loginEmail").send_keys(username)
# driver.find_element_by_id("loginPassword").send_keys(password)
# driver.find_element_css_selector("input[type=\"submit\"i]").click()

print("login success")