from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_frontend_backend_integration():
    driver = webdriver.Chrome()
    driver.get("http://192.168.49.2:30547")
    time.sleep(5)
    welcome_message_element = driver.find_element(By.TAG_NAME,"h1")
    welcome_message = welcome_message_element.text
    print("Welcome message:", welcome_message)
