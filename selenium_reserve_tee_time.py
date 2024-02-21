import os

from dotenv import dotenv_values
from rich import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def run():
    print('Starting Chrome driver')
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # open a browser window and go to the foreup login page
    driver.get(os.environ["FOREUP_SOFTWARE_LOGIN_URL"])

    # fill out the email input field
    driver.find_element(By.XPATH, '//*[@id="login_email"]').send_keys(os.environ["FOREUP_USERNAME"])
    driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(os.environ["FOREUP_PASSWORD"])

    # click the form log in button
    print("Attempting to log in")
    driver.find_element(By.XPATH, '//*[@name="login_button"]').click()

    # navigate to tee times page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#reservations-tab"))
    )
    print("Successfully logged in")
    driver.get(os.environ["FOREUP_SOFTWARE_TEETIMES_URL"])

    # click on Resident button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[ text() = "Resident (0 - 7 Days)" ]'))
    )
    driver.find_element(By.XPATH, '//*[ text() = "Resident (0 - 7 Days)" ]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#date"))
    )
    print("Calendar is there, find the calendar days which are not disabled")
    calendar_day_list = driver.find_elements(By.CSS_SELECTOR, ".day:not(.disabled)")

    print(f"Number of days available to reserve: {len(calendar_day_list)}")

    # the last non-disabled calendar day is the one we want to click on, so let's do it!
    last_available_day = calendar_day_list[-2]
    print(f"Last available day to reserve is: {last_available_day.text}, clicking it to bring up that date's tee times")
    last_available_day.click()

    # click on the # of players == 2 button to indicate we want 2
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.hidden-xs:nth-child(2) > a:nth-child(2)')))
    driver.find_element(By.CSS_SELECTOR, 'div.hidden-xs:nth-child(2) > a:nth-child(2)').click()

    # click on first available tee time
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='time time-tile']"))
    )
    first_tee_time = driver.find_element(By.XPATH, "//*[@class='time time-tile']")

    tee_time_info = first_tee_time.text.split("\n")
    print("\nFirst Tee Time Of Day Is:")
    print(
        f"Tee Time: {tee_time_info[0]} for {tee_time_info[1]} holes "
        f"with a max of {tee_time_info[2]} players "
        f"and the cost is: {tee_time_info[3]}\n\n"
    )

    first_tee_time.click()

    print("Attempting to book tee time")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-success"))
    )
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains('confirmation')
    )
    print("Successfully booked tee time!")
    driver.close()


if __name__ == "__main__":
    run()
