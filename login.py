import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def bypass_captcha(driver):
    ########################################################
    

    #######################################################
    # Find the captcha element.
    captcha_element = driver.find_element("id","g-recaptcha-response")

    # Create an ActionChains object.
    action_chains = ActionChains(driver)

    # Move the mouse to the captcha element.
    action_chains.move_to_element(captcha_element)

    # Click the captcha element.
    action_chains.click(captcha_element)

    # Release the mouse button.
    action_chains.release()

    # Perform the action chains.
    action_chains.perform()

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

    # Bypass the captcha.
    bypass_captcha(driver)

    # Find the login button.
    login_button = driver.find_element("id","btnSearch")

    # Click the login button.
    login_button.click()

def main():
    # Create a new Selenium WebDriver instance.
    driver = webdriver.Chrome()

    # Open the website.
    driver.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')

    # Login to the website.
    login(driver, '2200970140075', '02-07-2002')

    # Close the WebDriver instance.
    driver.quit()

if __name__ == '__main__':
    main()