import json
from pathlib import Path

from base_page import BasePage
from driver import get_chrome_driver
import schedule
import time

data_path = Path('config.json')


def get_file_data(filepath: Path) -> json:
    with open(filepath, 'r') as file:
        file_data = json.load(file)
    return file_data


def script(data_file_path):
    data = get_file_data(data_file_path)
    url = data["multisport_url"]
    username, password = data["credentials"]["username"], data["credentials"]["password"]
    cards = data["cards"]

    driver = get_chrome_driver()
    pages = BasePage(driver)
    driver.get(url)

    pages.username_field.find_element(assert_element=True)


schedule.every().saturday.at("14:00").do(script(data_path))
while True:
    schedule.run_pending()
    time.sleep(1)