from selenium import webdriver
import time
import pytest
import logging
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
@pytest.mark.parallel

def test_setting():
    capabilities = {
        "name": "test_vidya1",
        "browserName": "chrome",
        "version": "99.0",
        "cloudify:options": {
            "screenResolution": "1920x1080x24",
            "enableVideo": 'true',
            "enableLogs": 'true'
        }
    }

    driver = webdriver.Remote(command_executor=webdriver.remote.remote_connection.RemoteConnection
    ('https://2zb:ff65a2fe91d240eca379dabe806f019c@random-test-11.cloudifytests.io/wd/hub', resolve_ip=True),
                              desired_capabilities=capabilities)
    # driver = webdriver.Chrome(executable_path="D:\driver103\chromedriver.exe")
    # driver.maximize_window()
    driver.get("https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
    driver.find_element(By.XPATH, "(//input[@name='username'])[1]").send_keys("2zb")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='password'])[1]").send_keys("Hello123#")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='signInSubmitButton'])[1]").click()
    time.sleep(3)
    # driver.get("https://3tb.cloudifytests.io/")
    driver.find_element(By.XPATH, "(//span[text()='random-test-9']//following-sibling::div//button)[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()  # profile optn
    time.sleep(2)
    driver.find_element(By.XPATH, "(//li[@tabindex='-1'])[3]").click()  # setting option
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Chrome']").click()  # sellecting chrome browser
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@id='version-simple-select-standard']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[text()='100.0']").click()
    time.sleep(2)
    mannual_session_timeout = driver.find_element(By.XPATH, "//input[@type='number']")
    mannual_session_timeout.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    time.sleep(1)
    mannual_session_timeout.send_keys("15")
    time.sleep(2)
    session_timeout = driver.find_element(By.XPATH, "//input[@name='session_timeout']")
    session_timeout.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    session_timeout.send_keys("20")
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[text()='1920x1080']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='SAVE']").click()
    time.sleep(3)
    # driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()  # profile optn
    # time.sleep(1)
    # driver.find_element(By.XPATH, "(//li[@tabindex='-1'])[4]").click()     #logout option
    # time.sleep(1)
    driver.close()
