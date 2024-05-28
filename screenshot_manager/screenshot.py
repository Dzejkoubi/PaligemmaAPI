from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os


def take_screenshot(url, output_directory):
    # Replace "/" with "-" in the URL to save file correctly - when i saved it with / it wasnt saving the file correctly
    filename = url.replace("/", "-").replace(":", "").replace("?", "").replace("=", "").replace("&", "") + ".png"
    output_file_path = os.path.join(output_directory, filename)

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1920,1080")

    # Set up the WebDriver
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the page to load completely (you can increase the wait time if needed)
        driver.implicitly_wait(10)

        # Take a screenshot and save it
        driver.save_screenshot(output_file_path)
        print(f"Screenshot saved as {output_file_path}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # URL of the webpage to screenshot
    url = "https://borndigital.ai/cs/"  #Input URL

    # Output directory
    output_directory = "images"

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Take the screenshot
    take_screenshot(url, output_directory)
