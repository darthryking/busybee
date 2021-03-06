"""busybee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from ui import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='ui_index'),
    url(r'^dashboard/$', views.DashboardPage.as_view(), name='ui_dashboard'),
    url(r'^projects/$', views.ProjectPage.as_view(), name='ui_projects'),
    url(r'^tags/$', views.TagsPage.as_view(), name='ui_tags'),
]
