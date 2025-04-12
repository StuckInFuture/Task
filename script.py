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

    pages.privacy_agree_btn.click_if_visible()
    pages.username_field.find_element(assert_element=True)
    pages.login_btn.find_element(assert_element=True)

    pages.username_field.input_text(username)
    time.sleep(1)
    pages.password_field.input_text(password)
    time.sleep(2)
    pages.login_btn.wait_and_click()
    pages.progressbar.wait_for_element_to_disappear()
    pages.privacy_agree_btn.click_if_visible()
    pages.progressbar.wait_for_element_to_disappear()

    pages.location_address_dropdown_btn.find_element()
    loca = pages.location_address_field.find_element().text
    print(f"loc addr: {loca}")
    pages.privacy_agree_btn.click_if_visible(timeout=5_000)
    time.sleep(1)
    pages.submit_location_address_btn.wait_and_click()
    pages.progressbar.wait_for_element_to_disappear()
    time.sleep(1)
    pages.progressbar.wait_for_element_to_disappear()
    pages.register_with_multisport_card_btn.wait_and_click()
    pages.progressbar.wait_for_element_to_disappear()
    time.sleep(1)
    pages.card_number_input_field.input_text(cards[0])
    pages.progressbar.wait_for_element_to_disappear()
    pages.progressbar.wait_for_element_to_disappear()
    pages.accept_policies_checkbox.wait_and_click()
    pages.submit_service_btn.wait_and_click()
    pages.progressbar.wait_for_element_to_disappear()
    pages.progressbar.wait_for_element_to_disappear()
    time.sleep(100000)

    # time.sleep(1)
    # pages.register_with_multisport_card_btn.wait_and_click()
    # pages.progressbar.wait_for_element_to_disappear()
    # time.sleep(1)
    # pages.card_number_input_field.input_text(cards[0])
    # pages.progressbar.wait_for_element_to_disappear()
    # pages.progressbar.wait_for_element_to_disappear()
    # pages.accept_policies_checkbox.wait_and_click()
    # time.sleep(100000)



script(data_path)
# schedule.every().saturday.at("14:00").do(script(data_path))
# while True:
#     schedule.run_pending()
#     time.sleep(1)