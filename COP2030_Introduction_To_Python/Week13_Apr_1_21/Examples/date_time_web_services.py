# Learning about time and date
import time
from datetime import datetime, timedelta
import requests

#t = time.time()
#print(t)

#now = datetime.now()
#expires = datetime(2021, 3, 25)

#if now > expires:
#    print("Item expired")
#else:
#    print("Item not expired")

#now = datetime.now()
#tomorrow = now + timedelta(days=1)

#print(tomorrow)

# Look up real python website
# Learning about web services

base_url = 'https://jsonplaceholder.typicode.com'
resource = 'posts'
url = f'{base_url}/{resource}'

response = requests.get(url)
print(response.status_code)
#print(response.content)
data = response.json()
print(data[0])

#GET
#for post in data:
#    title = post['title']
#    print(f'Title: {title}')

#POST
blog_post = {
    'title': 'Hello Word',
    'body': 'This is the post body',
    'userId': 1
}

response = requests.post(url, json=blog_post)
print(response.status_code)
data = response.json()
print(data)
