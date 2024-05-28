from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os


def take_screenshot(url, output_file_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")    
    chrome_options.add_argument("window-size=1920,1080")
    
    
    # Set up the WebDriver
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the page to load completely
        driver.implicitly_wait(10)

        # Take a screenshot and save it
        driver.save_screenshot("images/" + "name.png" )
        print(f"Screenshot saved as {"images/" + "name.png" }")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # URL of the webpage to screenshot
    url = "https://borndigital.ai/cs/"  # Replace with your URL

    # Output file name
    output_filename = "screenshot.png"

    # Take the screenshot
    take_screenshot(url, output_filename)