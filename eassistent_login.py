import requests

# URL of the login page
login_url = 'https://www.easistent.com/p/ajax_prijava'

# URL of the main page
main_url = 'https://www.easistent.com/'

# URL of the calendar page
calendar_url = 'https://www.easistent.com/webapp#/calendar'

# User credentials
username = 'jon.pecar@gmail.com'
password = 'Vegova4.'

# Additional parameters
pin = ''
captcha = ''
skrij_znake_checkbox = False
koda = ''
force_sms = '1'  # This seems to be a flag used in the JavaScript code

# Data payload for the POST request
payload = {
    'uporabnik': username,
    'geslo': password,
    'pin': pin,
    'captcha': captcha,
    'skrij_znake': skrij_znake_checkbox,
    'koda': koda,
    'force_sms': force_sms
}

# Create a session
session = requests.Session()

# Send the login POST request
response = session.post(login_url, data=payload)

# Check the response
if response.ok:
    data = response.json()
    if data['status'] == 'ok':
        print('Login successful!')

        # Check if the response URL matches the main URL
        if response.url.startswith(main_url):
            print('Redirected to the main page.')

            # Access the calendar page using the session cookie
            calendar_response = session.get(calendar_url)
            if calendar_response.ok:
                print('Accessed the calendar page successfully.')
                # Print the HTML content of the calendar page
                print(calendar_response.text)
            else:
                print('Failed to access the calendar page:', calendar_response.status_code)
        else:
            print('Unexpected redirection after login:', response.url)
    else:
        print('Login failed:', data['message'])  # Print the error message
else:
    print('Failed to connect to the server.')
