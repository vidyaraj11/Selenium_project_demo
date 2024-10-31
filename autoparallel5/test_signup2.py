import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
@pytest.mark.parallel
# driver = webdriver.Chrome(executable_path="D:\driver103\chromedriver.exe")
# driver.maximize_window()
#time.sleep(1)
def test_signup2():
    capabilities = {
        "name": "test_vidyasignup2",
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
    driver.get("https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/signup?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
    driver.find_element(By.XPATH, "(//input[@name='username'])[2]").send_keys("vidya6")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='requiredAttributes[name]'])[2]").send_keys("vidya6")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@type='email'])[2]").send_keys("vidya6@mailinator.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='password'])[2]").send_keys("Hello123#")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//button[@name='signUpButton'])[2]").click()
    time.sleep(30)
    driver.find_element(By.XPATH, "//button[@name='confirm']").click()
    #driver.save_screenshot("C:\\Users\\Vidya raj\\PycharmProjects\\Demoproject\\test_signup2" + ".png")

    time.sleep(5)
    # driver.find_element(By.XPATH, "//button[text()='Create']").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH, "(//span[text()='200mb']//following-sibling::div//button)[2]").click()
    # time.sleep(3)
    driver.find_element(By.XPATH, "//input[contains(@id,'mui')]").send_keys("vidya6")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Create']").click()
    time.sleep(10)
    # driver.find_element(By.XPATH, "(//input[@value='10'])[2]")
    # time.sleep(2)
    # driver.find_element(By.XPATH, "(//input[@value='1'])[1]")
    # time.sleep(1)
    # driver.find_element(By.XPATH, "(//input[@value='1'])[2]")
    # time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4242424242424242")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='cardExpiry']").send_keys("0224")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='cardCvc']").send_keys("424")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billingName']").send_keys("Demo")
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[@value='US']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billingAddressLine1']").send_keys("sd")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billingAddressLine2']").send_keys("sd")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billingLocality']").send_keys("sd")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billingPostalCode']").send_keys("70000")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(130)
    isElement = driver.find_element(By.XPATH, "//span[text()='This site can’t be reached']").is_displayed()
    if isElement == 'true':
        print("successful")
    else:
        print("This site cannot be reached")
        time.sleep(10)
    driver.refresh()
    time.sleep(3)
    if isElement == 'true':
        print("successful")
    else:
        print("APPLICATION IS NOT LOADED")
        #driver.save_screenshot("C:\\Users\\Vidya raj\\PycharmProjects\\Demoproject\\test_signup2"+".png")
        time.sleep(4)
    driver.close()