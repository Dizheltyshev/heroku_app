from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class AddRemoveElementsPage:

    URL = "http://the-internet.herokuapp.com/add_remove_elements/"
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_add_element(self):
        self.driver.find_element(*self.ADD_BUTTON).click()

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.DELETE_BUTTON)


def test_add_remove_elements():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    page = AddRemoveElementsPage(driver)
    page.open()

    page.click_add_element()
    page.click_add_element()

    buttons = page.get_delete_buttons()
    assert len(buttons) == 2
    print(f"Добавили 2 кнопки DELETE")

    buttons[0].click()

    buttons_after = page.get_delete_buttons()
    assert len(buttons_after) == 1
    print(f"Удалили 1. Кнопок DELETE: {len(buttons_after)}")

    print("Тест завершен")
    driver.quit()


if __name__ == "__main__":
    test_add_remove_elements()