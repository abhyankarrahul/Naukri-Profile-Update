import os
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyautogui
import time


def update_naukri_profile():
    # Load environment variables from .env file
    dotenv.load_dotenv()

    # Set up the Selenium WebDriver (Chromium)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Maximize the browser window if not already maximized
        if not driver.get_window_rect()["width"] == driver.execute_script(
            "return screen.availWidth"
        ):
            driver.maximize_window()

        # Navigate to Naukri.com
        driver.get("https://www.naukri.com")

        # Log in to the Naukri account
        username = os.getenv("NAUKRI_USERNAME")
        password = os.getenv("NAUKRI_PASSWORD")

        # Ensure username and password are not None
        if not username:
            print("Error: NAUKRI_USERNAME environment variable is not set.")
            return
        if not password:
            print("Error: NAUKRI_PASSWORD environment variable is not set.")
            return

        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()

        # Wait for the username field to be visible and interactable
        try:
            username_field = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//input[@placeholder='Enter your active Email ID / Username']",
                    )
                )
            )
            # Scroll to the element to ensure it's interactable
            driver.execute_script("arguments[0].scrollIntoView(true);", username_field)
        except TimeoutException:
            print(
                "Error: Unable to locate or interact with the username field. Please verify the element's XPath or structure."
            )
            print("Page source for debugging:")
            print(driver.page_source)
            return

        # Wait for the password field to be present
        try:
            password_field = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@placeholder='Enter your password']")
                )
            )
        except TimeoutException:
            print(
                "Error: Unable to locate the password field. Please verify the element ID."
            )
            print("Page source for debugging:")
            print(driver.page_source)
            return

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Navigate to the profile page
        profile_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='view-profile-wrapper']")
            )
        )
        profile_button.click()

        # Update profile fields (example: updating headline)
        # profile_fields = os.getenv("PROFILE_FIELDS")  # Expected to be a JSON string
        # profile_data = eval(profile_fields)  # Convert JSON string to dictionary

        # for field_id, value in profile_data.items():
        #     field_element = wait.until(
        #         EC.presence_of_element_located((By.ID, field_id))
        #     )
        #     field_element.clear()
        #     field_element.send_keys(value)

        # Save the updated profile
        # save_button = wait.until(EC.element_to_be_clickable((By.ID, "saveButton")))
        # save_button.click()

        # Navigate to the resume upload section
        resume_upload_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Update resume']"))
        )
        resume_upload_button.click()

        # # Wait for the resume upload input field to be visible and interactable
        # try:
        #     upload_input = wait.until(
        #         EC.visibility_of_element_located((By.ID, "resumeUploadField"))
        #     )
        #     # Scroll to the element to ensure it's interactable
        #     driver.execute_script("arguments[0].scrollIntoView(true);", upload_input)
        # except TimeoutException:
        #     print(
        #         "Error: Unable to locate or interact with the resume upload field. Please verify the element's ID or structure."
        #     )
        #     print("Current URL:", driver.current_url)
        #     print("Page source for debugging:")
        #     print(driver.page_source.encode("utf-8", errors="replace").decode("utf-8"))
        #     return

        # Wait for the file upload dialog to appear
        time.sleep(2)  # Adjust the sleep time if needed

        # Ensure the file upload dialog is in focus
        pyautogui.click(
            x=500, y=500
        )  # Adjust coordinates to match the center of the dialog

        # Wait for the dialog to be ready
        time.sleep(2)  # Increase delay if needed

        # Debugging: Log the file path
        resume_file_path = os.getenv("RESUME_FILE_PATH")
        if not resume_file_path:
            print("Error: RESUME_FILE_PATH environment variable is not set.")
            return
        print("Typing file path:", resume_file_path)

        # Type the file path and press Enter
        pyautogui.write(resume_file_path)
        pyautogui.press("enter")

        # Save the updated resume
        # save_resume_button = wait.until(
        #     EC.element_to_be_clickable((By.ID, "saveResumeButton"))

        # save_resume_button.click()

        # Log out of the Naukri account
        logout_button_lines = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='nI-gNb-drawer__bars']")
            )
        )
        logout_button_lines.click()

        # Log out of the Naukri account
        logout_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='nI-gNb-list-cta' and @title='Logout']")
            )
        )
        logout_button.click()

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    update_naukri_profile()
    print("Profile updated successfully.")
    print("Logout successful.")
