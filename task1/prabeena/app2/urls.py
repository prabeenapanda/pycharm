from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [url(r'^admin/',admin.site.urls),
               url(r'^show/',views.gett),
               url(r'^add/',views.addd),
               ]