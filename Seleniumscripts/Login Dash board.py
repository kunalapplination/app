from selenium import webdriver
from selenium.webdriver.common.by import By
"import time"
import sys
driver = webdriver.Chrome(executable_path="C:\\Users\\Kunal\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
print(type(driver))
driver.maximize_window()
driver.get("https://avp-lg.applination.in/")
myPageTitle = driver.title
print(myPageTitle)
# assert "avp-lg.application.in" in myPageTitle
# print(driver.quit)
# driver.quit()
# from selenium.webdriver.common.by import By
# Login user id and Password
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div/form/input[1]").send_keys("neetu.gupta@vdoit.in")
driver.find_element(By.XPATH, "//html/body/div/div/div/section/div/div/form/input[2]").send_keys("123456")
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div/form/button").click()
time.sleep(2)
# Dashboard
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[1]/div[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[1]/div[2]/div/input").send_keys("Appli2022")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[2]/li/input").send_keys("90005")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[3]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/button").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[1]/input").send_keys("$50")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[2]/div").click()
driver.execute_script("window.scrollTo(0, 200)")
# driver.find_element_by_xpath("/html/body/div/div/div/div/div/section/form/div[4]/li[2]/div/ul/li[2]").send_keys("Wed");
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[2]/div/ul/li[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[3]/input").send_keys("02:30 PM")

driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[3]/input").send_keys("02:30 PM")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[4]/div").click()
time.sleep(1)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[4]/div/ul/li[2]").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[5]/input").send_keys("12/20/2022")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[4]/li[6]/input").send_keys("12/22/2022")
driver.execute_script("window.scrollBy(0, 200)")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[1]/div").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[1]/div/ul/li").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[2]/div").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[2]/div/ul/li[2]").click()
# Gender
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[3]/div").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[3]/div/ul/li[2]").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[4]/input").send_keys("10")
driver.execute_script("window.scrollBy(0, 200)")
# Indoor
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[5]/div").click()
time.sleep(0.5)
# driver.find_element_by_xpath("/html/body/div/div/div/div/div/section/form/div[5]/li[5]/div/ul/li[2]").click();
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[5]/div/ul/li[1]").click()
time.sleep(0.5)
# Preffared surface
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[6]/div").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[5]/li[6]/div/ul/li[2]").click()
# Division
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[6]/li/input").send_keys("3")
# rule
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[7]/li/div/a").click()
# create
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/span/button[2]").click()
time.sleep(768990000)
# Edit

# driver.execute_script("window.scrollTo(0, 800)")
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/span/button[1]").click()
# View in 1st division
# time.sleep(4)
# driver.find_element(By.XPATH, " /html/body/div/div/div/div/section[2]/div[6]/div/li/button").click()
# edit in setting in view division
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/span/button[2]").click()
# update in view division setting
# driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/span/button[2]").click()

# Dashboard
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[1]/div[3]/a").click()

time.sleep(5)
# Registration
driver.find_element(By.XPATH,"/html/body/div/div/div/nav/div/nav/ul/li[2]/a/span").click()
# Registration kunal demo1 New Team
time.sleep(7)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[2]/span/a/button").click()
# Kunal demo Name
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[1]/div[2]/input").send_keys("kunal")
# save button
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/section/form/div[2]/span/button[2]").click()
# Add team in division
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/section[2]/div[1]/div/div/div/div[2]/span[2]").click()
# add click in add team division
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div[1]/div[5]/button").click()
# Add click again kunal
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[5]/button").click()
# confirm click
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/button[2]").click()
time.sleep(6)

