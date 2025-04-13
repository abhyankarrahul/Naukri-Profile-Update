import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_update_naukri_profile():
    # Set up the Selenium WebDriver (Chromium)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Navigate to Naukri.com
        driver.get("https://www.naukri.com")

        # Log in to the Naukri account
        username = os.getenv("NAUKRI_USERNAME")
        password = os.getenv("NAUKRI_PASSWORD")

        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()

        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "usernameField"))
        )
        password_field = driver.find_element(By.ID, "passwordField")

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Navigate to the profile page
        profile_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My Naukri"))
        )
        profile_button.click()

        # Update profile fields (example: updating headline)
        profile_fields = os.getenv("PROFILE_FIELDS")  # Expected to be a JSON string
        profile_data = eval(profile_fields)  # Convert JSON string to dictionary

        for field_id, value in profile_data.items():
            field_element = wait.until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field_element.clear()
            field_element.send_keys(value)

        # Save the updated profile
        save_button = wait.until(EC.element_to_be_clickable((By.ID, "saveButton")))
        save_button.click()

        # Navigate to the resume upload section
        resume_upload_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Update Resume"))
        )
        resume_upload_button.click()

        # Upload the new resume
        resume_file_path = os.getenv("RESUME_FILE_PATH")
        upload_input = wait.until(
            EC.presence_of_element_located((By.ID, "resumeUploadField"))
        )
        upload_input.send_keys(resume_file_path)

        # Save the updated resume
        save_resume_button = wait.until(
            EC.element_to_be_clickable((By.ID, "saveResumeButton"))
        )
        save_resume_button.click()

        # Log out of the Naukri account
        logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_button.click()

    finally:
        # Close the browser
        driver.quit()
