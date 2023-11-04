import requests
from getpass import getpass
# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import whisper
import warnings
warnings.filterwarnings("ignore")

model = whisper.load_model("base")

def transcribe(url):
    with open('.temp', 'wb') as f:
        f.write(requests.get(url).content)
    result = model.transcribe('.temp')
    return result["text"].strip()

def click_checkbox(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

def request_audio_version(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()

def solve_audio_captcha(driver):
    text = transcribe(driver.find_element(By.ID, "audio-source").get_attribute('src'))
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
  
    driver.get("https://www.google.com/recaptcha/api2/demo")
    click_checkbox(driver)
    time.sleep(1)
    request_audio_version(driver)
    time.sleep(1)
    solve_audio_captcha(driver)
    time.sleep(10)
# Get user input
username = input("Enter your username: ")
email = getpass("Enter your email: ")  # Using getpass to securely input email

# Website URL and form data
url = "https://famoid.com/get-free-followers/"
data = {
    "username": username,
    "email": email
}

# Send a POST request to the website
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    print("Form submitted successfully!")
else:
    print("Failed to submit the form. Status code:", response.status_code)
