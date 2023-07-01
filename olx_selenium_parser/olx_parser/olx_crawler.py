import json
import time
from random import choice, randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from olx_parser.config import JSON_OUTPUT_FILE, DRIVER, LOGIN, PASSWORD


class AdsURLsReader:
    def __init__(self, path):
        self.path = path

    def read_urls(self):
        with open(self.path, "r", encoding="UTF-8") as file:
            return [url.strip() for url in file.readlines()]


class OLXLogin:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def execute(self, driver):
        time.sleep(3)
        login_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-2gs0sc"))
        )
        login_input.send_keys(self.login)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-ugcges"))
        )
        password_input.send_keys(self.password)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(10)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


class WebDriverConfigurator:
    def configure(self):
        options = webdriver.EdgeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-translate")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-sync")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-clipboard")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        return options


class AdsDataExtractor:
    def __init__(self, urls, user_agents):
        self.user_agents = user_agents
        self.urls = urls

    def extract_data(self):
        cookies = None
        user_agent = choice(self.user_agents)
        options = WebDriverConfigurator().configure()

        with webdriver.Edge(service=Service(DRIVER), options=options) as driver:
            driver.maximize_window()
            ads_results = []
            count = 0
            for url in self.urls[:5]:
                if count > 0 and count % 5 == 0:
                    print("[+] Sleeping to avoid detection...")
                    time.sleep(randint(75, 135))
                options.add_argument(f"user-agent={user_agent}")
                if cookies != None:
                    for cookie in cookies:
                        driver.add_cookie(cookie)
                driver.get(url)
                time.sleep(randint(45, 75))
                if self.urls.index(url) == 0:
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable(
                            (
                                By.CSS_SELECTOR,
                                "button[data-cy='dismiss-cookies-overlay']",
                            )
                        )
                    ).click()
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "css-12l1k7f"))
                    ).click()
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    OLXLogin(LOGIN, PASSWORD).execute(driver)
                    cookies = driver.get_cookies()
                    driver.get(url)

                try:
                    ads_title = driver.find_element(By.TAG_NAME, "h1").text.strip()
                except Exception:
                    ads_title = None
                try:
                    ads_price = driver.find_element(
                        By.CSS_SELECTOR, "h3.css-ddweki.er34gjf0"
                    ).text.strip()
                except Exception:
                    ads_price = None
                try:
                    ads_date = driver.find_element(
                        By.CSS_SELECTOR, "span.css-19yf5ek"
                    ).text.strip()
                except Exception:
                    ads_date = None
                try:
                    ads_description = driver.find_element(
                        By.CSS_SELECTOR, "div.css-bgzo2k"
                    ).text.strip()
                except Exception:
                    ads_description = None
                try:
                    all_photo_blocks = driver.find_elements(
                        By.CSS_SELECTOR, "div.swiper-slide.css-1915wzc"
                    )
                    ads_photo_urls = [
                        i.find_element(By.CSS_SELECTOR, "div.swiper-zoom-container img")
                        .get_attribute("src")
                        .strip()
                        for i in all_photo_blocks
                    ]
                except Exception:
                    ads_photo_urls = None
                try:
                    ads_seller_name = driver.find_element(
                        By.CSS_SELECTOR, "h4.css-1lcz6o7"
                    ).text.split()
                except Exception:
                    ads_seller_name = None
                # Получение номера телефона с кнопки "Показать" внизу страницы.
                if driver.find_elements(
                    By.XPATH, "//div[@data-testid='phones-container']"
                ):
                    try:
                        element = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, "css-19zjgsi"))
                        )
                        driver.execute_script("window.scrollBy(0, 150);")
                        ActionChains(driver).click(element).perform()
                        try:
                            WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located(
                                    (By.CLASS_NAME, "css-1478ixo")
                                )
                            )
                            find_phone_numbers = (
                                f"{elem.get_attribute('href').split(':')[-1]}"
                                for elem in driver.find_element(
                                    By.CLASS_NAME, "css-1478ixo"
                                ).find_elements(By.TAG_NAME, "a")
                            )
                            ads_seller_number = [
                                f"{i if i.startswith('+38') else f'+38{i}'}"
                                for i in find_phone_numbers
                            ]
                        except Exception:
                            driver.execute_script("window.scrollBy(0, 150);")
                            ActionChains(driver).click(element).perform()
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.CLASS_NAME, "css-1478ixo")
                                )
                            )
                            find_phone_numbers = (
                                f"{elem.get_attribute('href').split(':')[-1]}"
                                for elem in driver.find_element(
                                    By.CLASS_NAME, "css-1478ixo"
                                ).find_elements(By.TAG_NAME, "a")
                            )
                            ads_seller_number = [
                                f"{i if i.startswith('+38') else f'+38{i}'}"
                                for i in find_phone_numbers
                            ]
                    except Exception:
                        ads_seller_number = None
                else:
                    ads_seller_number = None
                if ads_seller_number == None:
                    try:
                        element = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, "css-1nd8q08"))
                        )
                        ActionChains(driver).click(element).perform()
                        try:
                            WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, "//span[@data-testid='primary-phone']")
                                )
                            )
                            find_phone_numbers = (
                                f"{elem.get_attribute('href').split(':')[-1]}"
                                for elem in driver.find_element(
                                    By.XPATH, "//span[@data-testid='primary-phone']/a"
                                )
                            )
                            ads_seller_number = [
                                f"{i if i.startswith('+38') else f'+38{i}'}"
                                for i in find_phone_numbers
                            ]
                        except Exception:
                            ActionChains(driver).click(element).perform()
                            WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, "//span[@data-testid='primary-phone']")
                                )
                            )
                            find_phone_numbers = (
                                f"{elem.get_attribute('href').split(':')[-1]}"
                                for elem in driver.find_element(
                                    By.XPATH, "//span[@data-testid='primary-phone']/a"
                                )
                            )
                            ads_seller_number = [
                                f"{i if i.startswith('+38') else f'+38{i}'}"
                                for i in find_phone_numbers
                            ]
                            webdriver.ActionChains(driver).send_keys(
                                Keys.ESCAPE
                            ).perform()  # тест нажатия на ескейп

                    except Exception:
                        ads_seller_number = None

                cookies = driver.get_cookies()
                print(
                    f"[+] Result: {self.urls.index(url)+1}/{len(self.urls)}. Number received: {ads_seller_number}"
                )
                count += 1
                ads_results.append(
                    {
                        "ads_url": url,
                        "ads_title": ads_title,
                        "ads_date": ads_date,
                        "ads_price": ads_price,
                        "ads_photos": ads_photo_urls,
                        "ads_description": ads_description,
                        "ads_seller_name": ads_seller_name,
                        "ads_seller_number": ads_seller_number,
                    }
                )
                with open(JSON_OUTPUT_FILE, "w", encoding="UTF-8") as file:
                    json.dump(ads_results, file, indent=4, ensure_ascii=False)
