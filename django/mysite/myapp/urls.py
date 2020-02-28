from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [url(r'^admin/',admin.site.urls),
               url(r'^show/',views.hello),
               url(r'^id/(\d+)/',views.id),
               url(r'^viewArticle/(\d{2})/(\d{4})',views.viewArticle),
               url(r'^email/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',
   views.sendemail),

]