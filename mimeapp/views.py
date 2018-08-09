from django.http import HttpResponse
data="<table><tr><th>eid</th><th>name</th><th>esal</th></tr><tr><td>1001</td><td>scott</td><td>2000</td></tr><tr><td>1002</td><td>blake</td><td>1500</td></tr><tr><td>1003</td><td>miller</td><td>2500</td></tr></table>"
def htmlview(request):
    return HttpResponse(data,content_type="text/html")
def xmlview(request):
    return HttpResponse(data,content_type="application/xml")
# Create your views here.
