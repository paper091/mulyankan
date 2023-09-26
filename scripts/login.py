import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def bypass_captcha(driver):
    ########################################################
    

    #######################################################
    # a-tcrwswf2nwx2
    # c-tcrwswf2nwx2

    driver.switch_to.default_content()
    # driver.switch_to.frame('/html/body/form/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/span/div/div/div/iframe')
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/form/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/span/div/div/div/iframe")))

    # Find the captcha element.
    captcha_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
    )

    # Create an ActionChains object.
    action_chains = ActionChains(driver)

    # Move the mouse to the captcha element.
    action_chains.move_to_element(captcha_element)

    # Click the captcha element.
    action_chains.click(captcha_element)

    # Release the mouse button.
    # action_chains.release()

    # Perform the action chains.
    action_chains.perform()
    driver.switch_to.default_content()


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

    #click somewhere else
    temp = driver.find_element(By.ID,"form1")
    temp.click()

    # Bypass the captcha.
    bypass_captcha(driver)

    # Find the login button.
    # login_button = driver.find_element("id","btnSearch")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnSearch"))).click()

    # Click the login button.
    # login_button.click()

def main():
    # Create a new Selenium WebDriver instance.
    driver = webdriver.Firefox()

    # Open the website.
    url = "https://erp.aktu.ac.in/webpages/oneview/oneview.aspx"
    driver.implicitly_wait(2)
    driver.get(url)

    # Login to the website.
    login(driver, '2200970140075', '02-07-2002')

    # Close the WebDriver instance.
    # driver.quit()

if __name__ == '__main__':
    main()