from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Kunal\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
print(type(driver))
driver.maximize_window()
driver.get("https://avp-lg.applination.in/")
# myPageTitle = driver.title
# print(myPageTitle)
# Login user id and Password
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div/form/input[1]").send_keys("neetu.gupta@vdoit.in")
driver.find_element(By.XPATH, "//html/body/div/div/div/section/div/div/form/input[2]").send_keys("123456")
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div/form/button").click()
time.sleep(2)
# Create players
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[1]/div[1]/a").click()
# work done click
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/ul/li[1]").click()
time.sleep(2)
# First Name
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[1]/div[2]/div[1]/input").send_keys("Kunal")
# Last Name
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[1]/div[2]/div[2]/input").send_keys("Kumar")
# DOB
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[2]/li[1]/input").send_keys("01/01/1991")
# Gender
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[2]/li[2]/div").click()
driver.execute_script("window.scrollTo(0, 100)")
# Male
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[2]/li[2]/div/ul/li[1]").click()
driver.execute_script("window.scrollTo(0, 100)")
# Shirt Size
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[1]/div").click()
# Shirt size click s
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[1]/div/ul/li[2]").click()
driver.execute_script("window.scrollTo(0, 200)")
# PREFERED SIDE click button
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[2]/div").click()
# prefared side right option
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[2]/div/ul/li[2]").click()
# Beach Experience click button
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[3]/div").click()
time.sleep(2)
# Beach experience Intermediate
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[3]/div/ul/li[2]").click()
# Position
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[4]/div").click()
time.sleep(1)
# Position (Blocker)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[4]/div/ul/li[1]").click()
# Dominant Hand click button
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[5]/div").click()
time.sleep(3)
# Domination hand (Left)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[5]/div/ul/li[1]").click()
# Height click button
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[6]/div").click()
# Height 6'4
driver.execute_script("window.scrollTo(0, 400)")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[3]/li[6]/div/ul/li[4]").click()
# School
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[4]/li/input").send_keys("IETE")
# Allergies
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[5]/li[1]/input").send_keys("Sand")
# Medical Issues
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[5]/li[2]/input").send_keys("Yes")
# Zip code
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[6]/li[1]/input").send_keys("9950")
# Phone
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[6]/li[2]/input").send_keys("7979099019")
# Email
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/form/div[6]/li[3]/input").send_keys("kunal@applination.in")
# cancle
driver.find_element(By.XPATH, "/html/body/div/div/div/div/span/button[1]").click()
# Save
time.sleep(3)
# New Team
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/span/a/button").click()
# Create Name kunal.sharma1
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[1]/div[2]/input").send_keys("Kunal.sharma1")
# Save button click
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[2]/span/button[2]").click()
time.sleep(2)
# New Team Creat again
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/span/a/button").click()
# Create name again kunal.2
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[1]/div[2]/input").send_keys("Kunal.2")
# Save button click
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[2]/span/button[2]").click()
