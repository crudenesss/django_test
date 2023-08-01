from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
import pdfkit, os
import urllib.request, json


def get_json():
    with urllib.request.urlopen("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=usd&sort=exchangedate&order=asc&json") as url:
        data = json.loads(url.read().decode('utf-8'))
    return data


def currency(request):
    template = loader.get_template('page.html')
    data = get_json()
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context))
    

def to_pdf(request):
    results = get_json()
    template = loader.get_template("layout.html")
    context = {"data": results, }  # data is the context data that is sent to the html file to render the output. 
    html = template.render(context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'currency.pdf')
    pdf = open("currency.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=currency.pdf'
    pdf.close()
    os.remove("currency.pdf")  # remove the locally created pdf file.
    return response


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
