import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up .env and selenium driver 
load_dotenv()
driver = webdriver.Chrome()
url = ("https://www.104.com.tw/jobs/main/")
driver.get(url)

# main page (without login)
driver.find_element(By.XPATH, '//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()

# login page
driver.find_element(By.ID, "username").send_keys(os.getenv("ACCOUNT"))
driver.find_element(By.ID, "password").send_keys(os.getenv("PASSWORD"))
driver.find_element(By.ID, "submitBtn").click()

# main page (with login)
WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "myName")))
driver.find_element(By.ID, "myName").click()
driver.find_element(By.XPATH, '//*[@id="global_bk"]/ul/li[2]/ul/li[4]/ul/li/div/dl/dt[1]/a').click()

# member center page
WebDriverWait(driver=driver, timeout=10).until(EC.new_window_is_opened)
name = driver.find_element(By.ID, "myName").text

# Check if username is correct
assert name == os.getenv("USERNAME"), f"Expected name is {os.getenv('USERNAME')}, but got {name}"
driver.find_element(By.XPATH, '//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a').click()
driver.close()
