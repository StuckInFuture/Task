import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_element(self, timeout=15_000, assert_element=False):
        try:
            if timeout == 0:
                element = self.driver.find_element(By.XPATH, self.locator)
            else:
                element = WebDriverWait(self.driver, timeout / 1_000).until(
                    EC.presence_of_element_located((By.XPATH, self.locator))
                )
            return element
        except Exception as ex:
            if assert_element:
                raise ex
            return None

    def input_text(self, text):
        self.find_element(assert_element=True).send_keys(text)

    def clear_field(self):
        self.find_element(assert_element=True).clear()

    def wait_and_click(self, timeout=15_000):
        try:
            element = WebDriverWait(self.driver, timeout / 1_000).until(
                EC.element_to_be_clickable((By.XPATH, self.locator)))
            element.click()
            return self
        except Exception as e:
            try:
                self.driver.find_element(By.XPATH, self.locator).click()
                return self
            except Exception as e:
                raise e

    def wait_for_element_to_disappear(self, timeout=15_000) -> bool:
        start_time = round(time.time() * 1000)
        while round(time.time() * 1000) - start_time < timeout:
            element = self.find_element(
                timeout=timeout
            )
            if element is None:
                return True
        return False
