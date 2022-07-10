from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def national(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=national"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['nationaldata'] = inshorts_data
    return render(request, 'national.html', records)

def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['businessdata'] = inshorts_data
    return render(request, 'business.html', records)

def world(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=world"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['worlddata'] = inshorts_data
    return render(request, 'world.html', records)

def politics(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=politics"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['politicsdata'] = inshorts_data
    return render(request, 'politics.html', records)

def technology(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=technology"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['technologydata'] = inshorts_data
    return render(request, 'technology.html', records)

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['entertainmentdata'] = inshorts_data
    return render(request, 'entertainment.html', records)
