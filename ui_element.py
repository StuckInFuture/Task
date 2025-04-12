import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class UIElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_element(self, timeout=15_000, assert_element=False):
        logging.info(f"TRYING TO FIND: {self.locator}")
        try:
            if timeout == 0:
                element = self.driver.find_element(By.XPATH, self.locator)
            else:
                element = WebDriverWait(self.driver, timeout / 1_000).until(
                    EC.visibility_of_element_located((By.XPATH, self.locator))
                )
            logging.info(f"Element found: {self.locator}")
            return element
        except Exception as ex:
            logging.info(f"Element was not found: {self.locator}")
            if assert_element:
                raise ex
            return None

    def input_text(self, text):
        logging.info(f"input text: {text}")
        self.find_element(assert_element=True).send_keys(text)

    def clear_field(self):
        self.find_element(assert_element=True).clear()

    def wait_and_click(self, timeout=15_000):
        logging.info(f"TRYING TO WAIT AND CLICK: {self.locator}")
        try:
            element = WebDriverWait(self.driver, timeout / 1_000).until(
                EC.element_to_be_clickable((By.XPATH, self.locator)))
            element.click()
            logging.info(f"Element was clicked: {self.locator}")
            return self
        except Exception as e:
            logging.info(f"Element for click was not found or clicked, one more attempt: {self.locator}")
            try:

                self.driver.find_element(By.XPATH, self.locator).click()
                logging.info(f"Element was clicked: {self.locator}")
                return self
            except Exception as e:
                raise e

    def wait_for_element_to_disappear(self, timeout=15_000) -> bool:
        logging.info(f"WAITING TO DISAPPEAR: {self.locator}")
        start_time = round(time.time() * 1000)
        while round(time.time() * 1000) - start_time < timeout:
            element = self.find_element(
                timeout=timeout
            )
            if element is None:
                logging.info(f"Element has disappeared: {self.locator}")
                return True
        logging.info(f"Element has not disappeared: {self.locator}")
        return False

    def click_if_visible(self, timeout=15_000):
        logging.info(f"TRYING TO CLICK IF VISIBLE: {self.locator}")
        element = self.find_element(timeout)
        if element:
            try:
                element.click()
                logging.info(f"Element was clicked: {self.locator}")
                return True
            except Exception as ex:
                logging.info(f"Element was not clicked: {self.locator}")
                pass
        return False
