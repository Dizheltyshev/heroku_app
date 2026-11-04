from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TyposPage:

    URL = "https://the-internet.herokuapp.com/typos"
    PARAGRAPH = (By.TAG_NAME, "p")

    CORRECT_TEXT = ["Sometimes you'll see a typo, other times you won't."]

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def refresh(self):
        self.driver.refresh()

    def get_paragraphs(self):
        return self.driver.find_elements(*self.PARAGRAPH)

    def get_second_paragraph_text(self):
        return self.get_paragraphs()[1].text


def test_typos():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    page = TyposPage(driver)
    page.open()

    typo_attempts = []

    for i in range(1, 11):
        text = page.get_second_paragraph_text()

        if text in page.CORRECT_TEXT:
            print(f"Попытка {i} без опечатки")
        else:
            print(f"Попытка {i} с опечаткой")
            typo_attempts.append(i)

        page.refresh()

    print()
    if typo_attempts:
        print(f"Опечатка встретилась на попытках: {typo_attempts}")
    else:
        print("За 10 обновлений опечатка не отобразилась")

    print("Тест завершен")
    driver.quit()

if __name__ == "__main__":
    test_typos()