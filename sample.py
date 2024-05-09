# this is a sample API call for the website chat

import requests

url = 'http://127.0.0.1:6000/survey'       # change the url to your link
data = {
    'role': 'Amazon Product Manager',
    'goal': 'Gather feedback from customers to enhance the user experience of the Amazon mobile app.'

}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

print(response.json())