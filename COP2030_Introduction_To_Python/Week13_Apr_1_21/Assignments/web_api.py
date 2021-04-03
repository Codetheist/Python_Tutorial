# ****************************************************************************************************
# Assignment # 7
# Program By: Antoine Gustave
# File Name: web_api.py
# Function: Use the "list users" api to print  just the email addresses of all users.
# Use the "register user" api to register a new user and print the status code of the operation.
# ******************************************************************************************************
import requests

base_url = 'https://reqres.in'
resource = 'api/users'
url = f'{base_url}/{resource}'
page = '/?page=2'

response = requests.get(url + page)
# print(get_response.status_code)
# print(get_response.content)
data = response.json()
# print(data)
emails = data["data"]

print('Email Requests')
print()

for email in emails:
    print(email["email"])

print()

print('New Users Request')
print()
create_user = {
    'name': 'Anthony Smith',
    'job': 'Python Dev',
}

response = requests.post(url, json=create_user)
print(response.status_code)
