#-*-coding:utf-8-*-
"""Bookmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bookapp.views.index',name='index'),

    url(r'^addbook.html/', 'bookapp.views.addbook0',name='addbook'),
    url(r'^addbook$', 'bookapp.views.addbook',name='addbook'),

    url(r'^addwriter.html/', 'bookapp.views.addwriter0',name='addwriter'),
    url(r'^addwriter$', 'bookapp.views.addwriter',name='addwriter'),

    url(r'^serchbook.html/', 'bookapp.views.serchbook0',name='serchbook'),
    url(r'^serchbook$', 'bookapp.views.serchbook',name='serchbook'),

    url(r'^serchwriter.html/', 'bookapp.views.serchwriter0',name='serchwriter'),
    url(r'^serchwriter$', 'bookapp.views.serchwriter',name='serchwriter'),

    url(r'^booklist.html/', 'bookapp.views.booklist',name='booklist'),
    url(r'^booklist$', 'bookapp.views.booklist',name='booklist'),
    
    url(r'^library$', 'bookapp.views.library',name='library'),

    url(r'^information$','bookapp.views.information',name='information'),

    url(r'^DelBook/(?P<key>[0-9]*)/$','bookapp.views.DelBook',name='DelBook'),
]

