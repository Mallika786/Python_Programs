import requests
import json

query=input("Enter what type of news you want to see?\n>>>")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-05-12&sortBy=publishedAt&apiKey=4bcbb675316844788f087a1263b0d936"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
      print(article["title"])
      print(article["description"])
      print("--------------------------------------")
