from django.shortcuts import render
from django.http import HttpRequest
from bs4 import BeautifulSoup
import feedparser

# Create your views here.
def index(request: HttpRequest):
    rss_feed_url = "https://vnexpress.net/rss/tin-moi-nhat.rss"
    feed = feedparser.parse(rss_feed_url)
    items_rss = []
    for item in feed.entries:
        title = item.get('title')
        link = item.get('link')
        pub_date = item.get('published')

        description = item.get('summary')
        description_soup = BeautifulSoup(description, 'html.parser')
        description_text = description_soup.get_text()

        image_tag = description_soup.find('img')
        image_src = image_tag["src"] if image_tag else ""

        items_rss.append( {
            'title': title,
            'link': link,
            'pub_date': pub_date,
            'description': description_text,
            'image_src': image_src
        })

    return render(request, 'index.html',  {
        'items_rss': items_rss
    })