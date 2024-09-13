from django.shortcuts import render
import requests

# Create your views here.
def news(request):
    response = requests.get("https://api.worldnewsapi.com/top-news?api-key=3722f173b5584020a63fcb8c3cd00330&source-country=us&language=en")
    news = response.json()["top_news"][0]["news"]
    return render(request, 'news/news.html', {"news": news})