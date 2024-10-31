import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
# @pytest.mark.login
@pytest.mark.parallel
def test_login():
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
    driver.find_element(By.XPATH, "(//input[@id='signInFormUsername'])[1]").send_keys("2zb")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@id='signInFormPassword'])[1]").send_keys("Hello123#")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='signInSubmitButton'])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//span[text()='random-test-9']//following-sibling::div//button)[2]").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()  # profile optn
    time.sleep(3)
    driver.find_element(By.XPATH, "(//li[@tabindex='-1'])[3]").click()  # setting option
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Chrome']").click()


    browser_name = driver.find_element(By.XPATH, "//span[text()='Chrome']").text
    print("browser on setting page:", browser_name)
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@id='version-simple-select-standard']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//li[text()='99.0']").click()

    time.sleep(1)
    browser_version = driver.find_element(By.XPATH, "(//input[@aria-hidden='true'])").get_attribute("value")

    print("browser_version on seting page", browser_version)
    time.sleep(2)
    mannual_session_timeout = driver.find_element(By.XPATH, "//input[@type='number']")
    mannual_session_timeout.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    time.sleep(1)
    mannual_session_timeout.send_keys("15")
    mannual_session_timeout1 = mannual_session_timeout.get_attribute("value")
    print("manual-session-timeout on setting:", mannual_session_timeout1)
    time.sleep(2)
    session_timeout = driver.find_element(By.XPATH, "//input[@name='session_timeout']")
    session_timeout.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    session_timeout.send_keys("20")
    session_timeout1 = session_timeout.get_attribute("value")
    print("session_timeout on setting page:", session_timeout1)
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[text()='1920x1080']").click()
    Resolution = driver.find_element(By.XPATH, "//li[text()='1920x1080']").text
    print("resolution on setting page", Resolution)

    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='SAVE']").click()
    time.sleep(2)
    # capabilities
    driver.find_element(By.XPATH, "//span[text()='Capabilities']").click()
    time.sleep(3)
    test_name = driver.find_element(By.XPATH, "//input[@id='standard-basic']")
    test_name.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    time.sleep(1)
    test_name.send_keys("test_vidya1")
    test_name_capabilities = driver.find_element(By.XPATH, "//input[@id='standard-basic']").get_attribute("value")
    print("test_name=", test_name_capabilities)
    time.sleep(3)
    selected_browser = driver.find_element(By.XPATH, "//span[text()='Chrome']").text
    print("browser_name on capabilities page", selected_browser)
    if browser_name == selected_browser:
        print("browser name is matched with setting:", selected_browser)
        time.sleep(2)
    else:
        print("browser is not matched")
    time.sleep(1)

    selected_version = driver.find_element(By.XPATH, "//div[text()='99.0']").text
    print("browser_version on capabilities page", selected_version)
    time.sleep(1)
    if browser_version == selected_version:
        print("browser_version is matched with setting:", browser_version)
        time.sleep(2)
    else:
        print("browser version is not matched")
    time.sleep(1)

    selected_resolution = driver.find_element(By.XPATH, "//li[text()='1920x1080']").text
    print("selected resolution on capabilities page", selected_resolution)
    if Resolution == selected_resolution:
        print("saved resolution matched:", Resolution)
        time.sleep(2)
    else:
        print("resolution is not matched")
    time.sleep(1)

    selected_mannual_session = driver.find_element(By.XPATH, "//input[@type='number']").get_attribute("value")
    print("selected mannual session timeout on capabilities page", selected_mannual_session)
    if mannual_session_timeout1 == selected_mannual_session:
        print("session timeout matched with saved:", mannual_session_timeout1)
        time.sleep(5)
    else:
        print("session timeout is not matched")
    time.sleep(1)
    #handle = driver.current_window_handle  # switch tab b/w 2 windows
    driver.find_element(By.XPATH, "//div[text()='Run Manually']").click()
    time.sleep(4)
    driver.close()
