from ui_element import UIElement


class BasePage:
    def __init__(self, driver):
        self.progressbar = UIElement(
            driver, "//div[contains(@class, 'loading')]"
        )
        self.privacy_agree_btn = UIElement(
            driver, "//button[contains(@id, 'didomi-notice-agree-button')]"
        )
        self.username_field = UIElement(
            driver, "//input[@id='username']"
        )
        self.password_field = UIElement(
            driver, "//input[@id='password']"
        )
        self.login_btn = UIElement(
            driver, "//input[contains(@class, 'btn') and @id='kc-login']"
        )
        self.submit_location_address_btn = UIElement(
            driver, "//button[@type='submit']"
        )
        self.location_address_dropdown_btn = UIElement(
            driver, "//div[@class='select valid']//img"
        )
        self.location_address_field = UIElement(
            driver, "//div[@class='select valid']//div[@class='selection']//div[@class='value']"
        )
        self.register_with_multisport_card_btn = UIElement(
            driver, "//div[contains(@class, 'card')]//a[contains(@href, 'card')]//button"
        )
        self.card_number_input_field = UIElement(
            driver, "//input[contains(@id, 'cardNumber')]"
        )
        self.choose_service_dropdown_btn = UIElement(
            driver, "//div[contains(@class, 'select')]//img"
        )
        self.accept_policies_checkbox = UIElement(
            driver, "//input[contains(@id, 'checkedIdentity')]"
        )
        self.submit_service_btn = UIElement(
            driver, "//button[@type='submit' and contains(@class, 'button')]"
        )
