import requests
from getpass import getpass

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
