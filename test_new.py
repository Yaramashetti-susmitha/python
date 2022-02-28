import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BasicTest:
    pass


class Test_Lambdatest(BasicTest):
    def test_first_scenario(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        tooltip = self.driver.find_element(By.XPATH, "//span[@class='cookie__bar__close hover:underline smtablet:hidden']")
        tooltip.click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Simple Form Demo']").click()
        url = self.driver.current_url
        if "simple-form-demo" in url:
            print("In simple form demo")
        else:
            print("No")

        message = "Welcome to LambdaTest"
        # print(message)
        self.driver.find_element(By.ID, "user-message").send_keys(message)
        self.driver.find_element(By.ID, "showInput").click()
        msg = self.driver.find_element(By.ID, "message").text
        print(msg)
        if msg == message:
            print("retrieving correct msg")
        else:
            print("No")
        self.driver.close()


    def test_second_scenario(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Drag & Drop Sliders']").click()
        range = self.driver.find_element(By.XPATH, "//div[@id='slider3']/div/input[@class='sp__range']")
        actions = ActionChains(self.driver)
        actions.click_and_hold(range).move_by_offset(112, 0).release().perform()
        verifyRange = self.driver.find_element(By.XPATH, "//div[@id='slider3']/div/output[@id='rangeSuccess']").text
        print(verifyRange)
        if verifyRange is range:
            print("correct range")
        else:
            print("Incorrect range")
        self.driver.close()

    def test_third_scenario(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[@class='cookie__bar__close hover:underline smtablet:hidden']").click()
        self.driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        nameelement = self.driver.find_element(By.ID, "name")
        errorMsg = self.driver.execute_script("return arguments[0].validationMessage;", nameelement)
        print(errorMsg)
        actualMessage = "Please fill in the fields."
        assert errorMsg, actualMessage
        self.driver.find_element(By.CSS_SELECTOR, '#name').send_keys("varma")
        self.driver.find_element(By.ID, 'inputEmail4').send_keys("varma@gmail.com")
        self.driver.find_element(By.ID, 'inputPassword4').send_keys("varma733")
        self.driver.find_element(By.ID, 'company').send_keys("lambda")
        self.driver.find_element(By.ID, 'website').send_keys("lambda-test.com")
        country = Select(self.driver.find_element(By.NAME, 'country'))
        country.select_by_visible_text("United States")
        self.driver.find_element(By.ID, 'inputCity').send_keys("Uluru")
        self.driver.find_element(By.ID, 'inputAddress1').send_keys("near petrol bunk")
        self.driver.find_element(By.ID, 'inputAddress2').send_keys("jambalaya street")
        self.driver.find_element(By.ID, 'inputState').send_keys("Andhra Pradesh")
        self.driver.find_element(By.ID, 'inputZip').send_keys("534112")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        msg = "Thanks for contacting us, we will get back to you shortly."
        hidMsg = self.driver.find_element(By.CSS_SELECTOR, "p[class='success-msg hidden']").text
        if hidMsg == msg:
            print(hidMsg)
        else:
            print("Not as expected")
        self.driver.close()