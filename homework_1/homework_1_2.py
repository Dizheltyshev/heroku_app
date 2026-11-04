from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class CheckboxesPage:

    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "[type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)


def test_checkboxes():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    page = CheckboxesPage(driver)
    page.open()

    first = page.get_checkboxes()[0]
    assert first.is_selected() is False
    print("Первый чекбокс unchecked")

    first.click()

    first = page.get_checkboxes()[0]
    assert first.is_selected() is True
    print("Первый чекбокс стал checked")

    second = page.get_checkboxes()[1]
    assert second.is_selected() is True
    print("Второй чекбокс checked")

    second.click()

    second = page.get_checkboxes()[1]
    assert second.is_selected() is False
    print("Второй чекбокс стал unchecked")

    print("Тест завершен")
    driver.quit()


if __name__ == "__main__":
    test_checkboxes()