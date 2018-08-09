from django.conf.urls import url
from .import views
app_name='mimeapp'
urlpatterns=[
    url(r'^html$',views.htmlview,name='htmlview'),
    url(r'^xml$',views.htmlview,name='xmlview'),
            ]