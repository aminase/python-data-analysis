from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 


service = Service(executable_path="/Users/admin/Desktop/analysis/chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://www.geeksforgeeks.org/")

dropdown = driver.find_element(By.LINK_TEXT, "Data Science")
dropdown.click()
print(dropdown)




time.sleep(5)
driver.quit()
