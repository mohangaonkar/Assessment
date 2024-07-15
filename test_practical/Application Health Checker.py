# 4. Application Health Checker:
# Please write a script that can check the uptime of an application and
# determine if it is functioning correctly or not. The script must accurately
# assess the application's status by checking HTTP status codes. It should be
# able to detect if the application is 'up', meaning it is functioning correctly, or
# 'down', indicating that it is unavailable or not responding.



import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        # Checking the status code indicates the application is up
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"Error checking application health: {e}")
        return 'down'


if __name__ == "__main__":
    # Example I have taken of a website
    application_url = "https://demo.nopcommerce.com/login?returnUrl=%2F"

    status = check_application_health(application_url)
    print(f"The application is {status}.")