# library to read api
import requests
import send_email

topic = "tesla"

api_key = "8d6b19fe265341c1b929dbcdac6d8810"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-04-14 \ " \
      "&sortBy=publishedAt&apiKey=8d6b19fe265341c1b929dbcdac6d8810&" \
      "language=en"

# Make a request
requests = requests.get(url)
# content is text
# content = requests.text

# Get a dictionary with data
# content is json
content = requests.json()

body = ""
# Access the article titles and description
for article in content['articles'][0:20]:
      if article["title"] is not None:
          body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
                 + article["description"] + "\n" \
                 + article["url"] + 2*"\n"

body = body.encode("utf-8")
# input should be a string
send_email.send_email(body)
