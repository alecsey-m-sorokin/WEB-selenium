from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def open_site(self, url: str) -> None:
        """ Открытие страницы по url """
        self.driver.get(url)

    def get(self, url):
        return self.driver.get(url)

    def close(self):
        return self.driver.close()

    def quit(self):
        return self.driver.quit()

    def switch_to_frame(self, locator) -> None:
        self.driver.switch_to.frame(WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(locator),
                                                                        message=f"Невозможно переключиться на iframe с локатором - {locator}"))

    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    def find_element_presence(self, locator, delay=10):
        # Finds one presence_of_element by locator
        return WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find presence_of_element with locator {locator}.")

    def find_elements_presence(self, locator, delay=10):
        # Finds presence_of_all_elements by locator
        return WebDriverWait(self.driver, delay).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find presence_of_all_elements with locator {locator}.")

    def find_element_visibility(self, locator, delay=10):
        # Finds one visibility_of_element by locator
        return WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(locator),
                                                       message=f"Can't find visibility_of_element with locator {locator}.")

    def find_all_elements_presence_by_locator(self, locator) -> list:
        # Finds all elements presence by locator
        __data = []
        results = self.find_elements_presence(locator)
        print(f'\n')
        print(f'found {len(results)} elements by locator = {locator}')
        for element in results:
            print(element)
            __data.append(element)
        return __data

    def check_exists_in_page_source(self, source) -> bool:
        import re

        src = self.driver.page_source
        text_found = re.search(rf"{source}", src)
        print(f"result = {text_found}")
        if text_found is None:
            print(f'искомое значение "{source}" не найдено')
            return False
        else:
            print(f'искомое значение "{source}" найдено')
            return True
