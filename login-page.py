# test_login_selenium.py
"""
Selenium script to test a login page.
Adjust URL, selectors, and credentials to your app.
Requires: pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

def run_login_test(base_url, username, password, selectors):
    """
    selectors: dict with keys 'user', 'pass', 'submit', 'success_indicator', 'error_indicator'
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(base_url)
    time.sleep(1)  # wait for page to load (use WebDriverWait in production)

    # valid login attempt
    driver.find_element(By.CSS_SELECTOR, selectors['user']).clear()
    driver.find_element(By.CSS_SELECTOR, selectors['user']).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, selectors['pass']).clear()
    driver.find_element(By.CSS_SELECTOR, selectors['pass']).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, selectors['submit']).click()
    time.sleep(1)

    success = False
    try:
        if selectors.get('success_indicator') and driver.find_elements(By.CSS_SELECTOR, selectors['success_indicator']):
            success = True
    except Exception:
        success = False

    driver.save_screenshot('login_valid_result.png')

    # invalid login attempt
    driver.get(base_url)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, selectors['user']).clear()
    driver.find_element(By.CSS_SELECTOR, selectors['user']).send_keys("wrong_user")
    driver.find_element(By.CSS_SELECTOR, selectors['pass']).clear()
    driver.find_element(By.CSS_SELECTOR, selectors['pass']).send_keys("wrong_pass")
    driver.find_element(By.CSS_SELECTOR, selectors['submit']).click()
    time.sleep(1)

    error_present = False
    try:
        if selectors.get('error_indicator') and driver.find_elements(By.CSS_SELECTOR, selectors['error_indicator']):
            error_present = True
    except Exception:
        error_present = False

    driver.save_screenshot('login_invalid_result.png')
    driver.quit()

    return {"valid_login_success": success, "invalid_login_error_shown": error_present}


if __name__ == "__main__":
    BASE_URL = "https://example.com/login"  # replace with your login URL
    SELECTORS = {
        "user": "input[name='username']",
        "pass": "input[name='password']",
        "submit": "button[type='submit']",
        # update these to the element that appears on success/failure
        "success_indicator": "div.dashboard, .welcome-msg",
        "error_indicator": ".error, .alert-danger"
    }
    results = run_login_test(BASE_URL, "testuser", "correct_password", SELECTORS)
    print("Test results:", results)
