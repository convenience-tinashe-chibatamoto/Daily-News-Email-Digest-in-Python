import requests
from send_email import send_email

api_key = "0a16379b1db84fd6a69dd27ff09bafad"
url = "https://newsapi.org/v2/everything?q=nvdia&" \
      "sortBy=publishedAt&apiKey=" \
      "0a16379b1db84fd6a69dd27ff09bafad"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)