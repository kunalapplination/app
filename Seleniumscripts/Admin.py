
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

'from selenium.webdriver.common.by import By'
'import time'
driver = webdriver.Chrome(executable_path="C:\\Users\\Kunal\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://avp-lg.applination.in/")
# Login user id and Password
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div/form/input[1]").send_keys("neetu.gupta@vdoit.in")
driver.find_element(By.XPATH, "//html/body/div/div/div/section/div/div/form/input[2]").send_keys("123456")
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div/form/button").click()
time.sleep(3)
# Admin
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div/div/div/nav/div/nav/ul/li[4]/a/span").click()
# Managers
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/ul/li[1]").click()
# edit
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[2]/div/div[2]/div[6]/button").click()
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(6)
# edit in workday 1
driver.find_element(By.XPATH, "/html/body/div/div/div/div/span/button[1]").click()
# Go division view
# time.sleep(5)
#  driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[6]/div/li[1]/button").click()
# time.sleep(7)
# edit in view
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/span/button[2]").click()
# update
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/span/button[2]").click()
# location in go division
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[2]/li/div").send_keys("")
# set division view
# time.sleep(6)
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[6]/div/li[2]/button").click()
# edit in view set division
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/span/button[2]").click()
# update in set division view edit ,update
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/span/button[2]").click()
# edit in workday 1
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/span/button[1]").click()
# update
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/span/button[2]").click()
