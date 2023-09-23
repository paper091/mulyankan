# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
 
# create webdriver object
driver = webdriver.Firefox()

# for waiting for dynamic html updates
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
# get geeksforgeeks.org
url = "https://erp.aktu.ac.in/webpages/oneview/oneview.aspx"
driver.implicitly_wait(2)
driver.get(url)
 
# get element
roll_container = driver.find_element(By.ID, "txtRollNo")
continue_btn = driver.find_element(By.ID, "btnProceed")

 
# send keys
roll_container.send_keys("2200970140074")

# create action chain object
action = ActionChains(driver)
action.click(on_element = continue_btn)
action.perform()

#############
#  next page
#############

# driver.refresh()
# driver.switch_to.frame("content")
DOB_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtDOB"))
    )
DOB_container.send_keys("19/10/2001")

div = driver.find_element(By.CLASS_NAME, "container-login100")
action.click(on_element = div)
action.perform()

# recaptcha = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
#     )
# action.click(on_element = recaptcha)
# action.perform()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

searchBtn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(("btnSearch", 'enabled_trigger'))
    )
searchBtn.click()



# searchBtn = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "btnSearch"))
#     )
# action.click(on_element= searchBtn)
# action.perform()