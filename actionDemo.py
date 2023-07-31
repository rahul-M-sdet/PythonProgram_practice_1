from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By

service_obj=Service(r"C:\Users\RAHUL\Downloads\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://paytm.com/")
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Paytm For Business")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Business Payments")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Payouts")).click().perform()

# action.move_to_element(driver.find_element(By.CLASS_NAME,"_2dve7")).perform()
# action.context_click(driver.find_element(By.CLASS_NAME,"_3y5vS")).click().perform()


