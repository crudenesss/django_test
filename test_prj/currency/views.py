from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def currency(request):
    template = loader.get_template('page.html')
    return HttpResponse(template.render())

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
