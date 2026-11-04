from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InputsPage:

    URL = "https://the-internet.herokuapp.com/inputs"
    INPUT = (By.TAG_NAME, "input")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_input(self):
        return self.driver.find_element(*self.INPUT)

    def type_value(self, value):
        self.get_input().send_keys(value)

    def press_arrow_up(self):
        self.get_input().send_keys(Keys.ARROW_UP)

    def press_arrow_down(self):
        self.get_input().send_keys(Keys.ARROW_DOWN)

    def get_value(self):
        return self.get_input().get_attribute("value")


def test_inputs():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    page = InputsPage(driver)
    page.open()

    page.type_value("2")
    assert page.get_value() == "2"
    print(f"Ввели: {page.get_value()}")

    page.press_arrow_up()
    assert page.get_value() == "3"
    print(f"После ARROW_UP: {page.get_value()}")

    page.press_arrow_down()
    assert page.get_value() == "2"
    print(f"После ARROW_DOWN: {page.get_value()}")

    print("Тест завершен")
    driver.quit()


if __name__ == "__main__":
    test_inputs()