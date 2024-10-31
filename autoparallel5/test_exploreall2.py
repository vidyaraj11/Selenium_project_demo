import pytest
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
@pytest.mark.parallel
# driver = webdriver.Chrome(executable_path="D:\driver103\chromedriver.exe")
# driver.maximize_window()

def test_explore_all():
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
    driver.get("https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
    driver.find_element(By.XPATH, "(//input[@id='signInFormUsername'])[1]").send_keys("1zb")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@id='signInFormPassword'])[1]").send_keys("Hello123#")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='signInSubmitButton'])[1]").click()
    time.sleep(3)

    organisation_list = ["15tb", "qwerr", "337mb", "10fb", "11fb", "12re", "121gb"]
    # print(organisation_list)
    organisation_length = len(organisation_list)
    print(organisation_length)
    for x in range(organisation_length):
        # (//button[text()='Explore'])[1]
        driver.find_element(By.XPATH, "(//button[text()='Explore'])[" + str(x + 1) + "]").click()
        # driver.find_element(By.XPATH, "(//span[text()='x']//following-sibling::div//button)[2]").click()
        time.sleep(2)
        try:
            if driver.find_element(By.XPATH, "//div[text()='Creating Organisation']").text == "Creating Organisation":
                print(organisation_list[x], "createing_org")
                # time.sleep(4)
                # if createing_org == "Creating Organisation":
                time.sleep(3)
                driver.back()
                # print("clicked on back")
                time.sleep(3)
        except:
            if driver.find_element(By.XPATH, "//span[text()='Sessions']").text == "Sessions":
                time.sleep(2)
                print("Title of the page:", driver.title)
                time.sleep(2)
                print("URL of the page:", driver.current_url)
                driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()  # profile optn
                time.sleep(2)
                driver.find_element(By.XPATH, "(//li[@tabindex='-1'])[2]").click()  # manage plan option
                time.sleep(2)
                # parallel_session = driver.find_element(By.XPATH, "//div[text()='10']").text  # ||el session
                # print("total number of parallel session:", parallel_session)
                # time.sleep(2)
                Retention_period = driver.find_element(By.XPATH, "//div[text()='27 Jul 2022']").text
                print("Retention period on:", Retention_period)
                time.sleep(2)
                Plan_period = driver.find_element(By.XPATH, "//div[text()='27 Jul 2022']").text
                print("plan period upto:", Plan_period)
                time.sleep(2)
                driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()  # profile optn
                time.sleep(2)
                driver.find_element(By.XPATH, "(//li[@tabindex='-1'])[1]").click()  # view orgntsn option
                time.sleep(3)
    driver.close()