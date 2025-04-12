from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--enable-automation")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")
    user_agent = UserAgent(browsers="chrome", os="Mac OS X", platforms="desktop").random
    chrome_options.add_argument(
        f"user-agent='{user_agent}'"
    )
    print("Driver installation")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver


def stop_driver(driver):
    try:
        if driver is None:
            pass
        else:
            driver.quit()
    except Exception as ex:
        print(f"Exception: cannot stop driver {ex.__str__()}")

