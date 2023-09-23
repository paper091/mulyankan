import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select
import time

def find_all_iframes(driver):
    iframes = driver.find_element("xpath","//iframe")
    for index, iframe in enumerate(iframes):
        # Your sweet business logic applied to iframe goes here.
        driver.switch_to.frame(index)
        find_all_iframes(driver)
        driver.switch_to.parent_frame()

def bypass_captcha(driver):
    ########################################################
    

    #######################################################
    print("crash")

    # back to default web page frame
    driver.switch_to.default_content()

    driver.switch_to.frame("/html/body/form/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/span/div/div/div/iframe")

    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,'//*[@id="pnlCaptcha"]/span/div/div/div/iframe')))
    driver.find_element('xpath', "/html/body/div[2]/div[3]/div[1]/div/div/span").click()


    
    # back to default web page frame
    driver.switch_to.default_content()

    # # Find the captcha element.
    # captcha_element = driver.find_element("id","g-recaptcha-response")

    # # Create an ActionChains object.
    # action_chains = ActionChains(driver)

    # # Move the mouse to the captcha element.
    # action_chains.move_to_element(captcha_element)

    # # Click the captcha element.
    # action_chains.click(captcha_element)

    # # Release the mouse button.
    # action_chains.release()

    # # Perform the action chains.
    # action_chains.perform()

def login(driver, username, password):
    # Find the username field.
    username_field = driver.find_element("id","txtRollNo")

    # Enter the username.
    username_field.send_keys(username)

    # Find the proceed button.
    proceed_button = driver.find_element("id","btnProceed")

    # Click the proceed button.
    proceed_button.click()

    # Find the password field.
    password_field = driver.find_element("id", "txtDOB")

    # Enter the password.
    password_field.send_keys(password)

    print("crash")

    # Bypass the captcha.
    bypass_captcha(driver)

    print("crash")

    # # Find the login button.
    # login_button = WebDriverWait(driver, 20).until(
    # EC.element_to_be_clickable(("btnSearch", 'enabled_trigger'))
    # )

    # # Click the login button.
    # login_button.click()

def main():
    # Create a new Selenium WebDriver instance.
    driver = webdriver.Chrome()

    # Open the website.
    driver.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')

    find_all_iframes(driver)

    # Login to the website.
    login(driver, '2200970140075', '02-07-2002')

    # # Close the WebDriver instance.
    # driver.quit()

if __name__ == '__main__':
    main()