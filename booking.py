import datetime
import pause

import selenium.common.exceptions
from selenium import webdriver
from navigator import Navigator


def booking(date, hour, court_num, username, password):
    home_url = "https://recreation.utoronto.ca/booking"
    booking_time = compute_booking_time(date, hour)
    print(f"\nThe court booking bot will try to book the earliest possible court two days from {booking_time}. \n")

    pause.until(booking_time - datetime.timedelta(minutes=5))

    driver = webdriver.Chrome()

    try:
        navigator = Navigator(driver)
        navigator.goto(home_url)
        navigator.login(username, password)
        navigator.book_court(booking_time, court_num)
        print("\nSuccessfully booked a court!")
    except selenium.common.exceptions.TimeoutException:
        print("\nDid not manage to book a court :(")


def compute_booking_time(date, hour):
    return datetime.datetime.strptime(date, "%d/%m/%Y") - datetime.timedelta(days=2) + datetime.timedelta(hours=hour)