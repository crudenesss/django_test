from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import urllib.request, json
import pandas as pd

# Create your views here.

def currency(request):
    template = loader.get_template('page.html')
    with urllib.request.urlopen("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=usd&sort=exchangedate&order=asc&json") as url:
        data = json.loads(url.read().decode('utf-8'))
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
