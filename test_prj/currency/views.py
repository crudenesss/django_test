from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import urllib.request, json

from xhtml2pdf import pisa
# from django.template import Context

# Create your views here.

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
    
"""def to_pdf(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    data = get_json()

    p.drawString("".join(data))

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True)"""
    
def render_pdf(template_src, context_dict):
    template = loader.get_template(template_src)
    #context = Context(context_dict)
    #html  = template.render(context)
    html = render_to_string(template_src, context_dict)
    result = io.BytesIO()

    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)
    return HttpResponse(result.getvalue(), content_type='application/pdf')
    
def to_pdf(request):
    results = get_json()
    return render_pdf(
            'layout.html',
            {
                'pagesize':'A4',
                'data': results,
            }
        )

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
