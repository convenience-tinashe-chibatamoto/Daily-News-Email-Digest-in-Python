import requests
import os

my_secret = os.environ['API_KEY']
url = "https://newsapi.org/v2/everything?q=nvidia&" \
      "sortBy=publishedAt&apiKey=" \
      "0a16379b1db84fd6a69dd27ff09bafad"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
  print(article["title"])
  print(article["description"])
