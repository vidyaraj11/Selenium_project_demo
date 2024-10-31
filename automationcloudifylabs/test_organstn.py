from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def Test_org():
    driver = webdriver.Chrome(executable_path="D:\driver103\chromedriver.exe")
    driver.maximize_window()
    driver.get(
        "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
    driver.find_element(By.XPATH, "(//input[@name='username'])[2]").send_keys("98mb")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='password'])[2]").send_keys("Hello123#")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//input[@name='signInSubmitButton'])[2]").click()
    time.sleep(3)
    # driver.get("https://3tb.cloudifytests.io/")
    driver.find_element(By.XPATH, "(//span[text()='200mb']//following-sibling::div//button)[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()  # profile optn
    time.sleep(2)
    driver.find_element(By.XPATH, "(//li[@tabindex='-1'])[3]").click()  # setting option
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Chrome']").click()  # sellecting chrome browser
    time.sleep(10)
    # select=Select(driver.find_elements(By.XPATH, "//div[@id='version-simple-select-standard']"))
    # a=driver.find_elements(By.XPATH, "//ul[@tabindex='-1']")
    # print(len(a))
    # select.select_by_visible_text("100.0")
    # assert "100.0" in select.first_selected_option.text
    # time.sleep(6)
    driver.find_element(By.XPATH, "//input[@type='number']").send_keys("15")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='session_timeout']").send_keys("20")
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[text()='1920x1080']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='SAVE']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//li[text()='Log out']").click()
    time.sleep(1)
    driver.close()