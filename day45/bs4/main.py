from bs4 import BeautifulSoup
import requests

link = "https://news.ycombinator.com/news"
response = requests.get(link)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(class_="titleline")

article_upvotes = [int(f.getText().split()[0]) for f in soup.find_all(class_="score")]
article_upvotes_max = max(article_upvotes)
article_upvotes_max_index = article_upvotes.index(article_upvotes_max)
article_texts = [f.a.getText() for f in articles]
article_links = [f.a.get('href')for f in articles]

print(article_texts[article_upvotes_max_index])
print(article_links[article_upvotes_max_index])
print(article_upvotes_max)
