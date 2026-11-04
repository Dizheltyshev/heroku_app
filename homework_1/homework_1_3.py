from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownPage:

    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_select(self):
        return Select(self.driver.find_element(*self.DROPDOWN))


def test_dropdown():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    page = DropdownPage(driver)
    page.open()
    select = page.get_select()

    all_options = select.options
    assert len(all_options) > 0, "В дропдауне нет вариантов"
    print(f"Найдено вариантов: {len(all_options)}")

    select.select_by_index(1)
    assert select.first_selected_option.text == "Option 1"
    print("Выбран Option 1")

    select.select_by_index(2)
    assert select.first_selected_option.text == "Option 2"
    print("Выбран Option 2")

    print("Тест завершен")
    driver.quit()


if __name__ == "__main__":
    test_dropdown()