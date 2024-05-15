import requests
from send_email import send_email

topic = "nvdia"

api_key = "0a16379b1db84fd6a69dd27ff09bafad"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
      "sortBy=publishedAt" \
      "&apiKey=0a16379b1db84fd6a69dd27ff09bafad" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:11]:
    if article["title"] is not None:
        body = "Subject: Convenience's Email Digest" + "\n" + body + article["title"] + "\n" \
      + str(article["description"]) \
      + "\n" + str(article["url"]) + "\n\n"
        + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
