from selenium import webdriver
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C://Users//Neha//PycharmProjects//selenium//Driver//chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield
    driver.close()
    driver.quit()
    print("Test completed")
def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
#assertion allows the correctnes of the output. if it fails an error msg will be displayd.
    x = driver.title
    assert x == "OrangeHRM"
