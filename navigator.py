import selenium
import time
import pause

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Navigator:
    def __init__(self, driver: selenium.webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 1)

    def goto(self, link):
        self.driver.get(link)

    def login(self, username, password):
        login_button = self.driver.find_element(By.XPATH, "//a[text()='Sign In']")
        login_button.click()
        time.sleep(1)
        self.wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth")
        )).click()
        self.wait.until(expected_conditions.presence_of_element_located(
            (By.ID, "username")
        )).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg").click()
        time.sleep(20)

    def refresh_page(self):
        try:
            self.driver.refresh()
        except Exception:
            print("Driver quit unexpectedly!")

    def book_court(self, booking_time, court_num):
        # Hard-coded links to each badminton court's booking site, but user needs to be authenticated first!
        if court_num == 1:
            court_listing = "https://recreation.utoronto.ca/booking/af97abfd-f094-49c4-8a17-9330879ed6cc"
        if court_num == 2:
            court_listing = "https://recreation.utoronto.ca/booking/08ec6e7c-068d-4875-94a2-178ddef80b9b"
        if court_num == 3:
            court_listing = "https://recreation.utoronto.ca/booking/c8f30b5c-8c2c-4d9e-bb7c-bb214bc94c7d"
        self.driver.get(court_listing)

        # Wait until we reach the hour before we try to book the court
        pause.until(booking_time)

        # Try 3 times to book the court
        for i in range(3):
            try:
                self.driver.refresh()
                time.sleep(0.5)
                self.wait.until(expected_conditions.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "button.btn.single-date-select-button.single-date-select-one-click.btn-secondary"))
                )[1].click()
                time.sleep(0.5)
                self.wait.until(expected_conditions.presence_of_all_elements_located(
                    (By.XPATH, "//button[text()='Book Now']")
                ))[-1].click()
                success = True
            except TimeoutException:
                continue
            if success:
                return
        raise TimeoutException
