"""
high level support for doing this and that.
"""



from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time


service = Service(executable_path="/Users/admin/Desktop/analysis/chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://google.com")
time.sleep(30)
driver.quit()



