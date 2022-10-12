from django.urls import re_path as url

from Wand import views

urlpatterns = [
    url(r'^tip$', views.tipsApi),
    url(r'^tip/([0-9]+)$', views.tipsApi),
    url(r'^shaft$', views.shaftsApi),
    url(r'^shaft/([0-9]+)$', views.shaftsApi)
]
