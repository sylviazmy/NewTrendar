"""Trendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dashboard_views.index, name='home'),
    url(r'^in/', dashboard_views.whatsin, name='in'),
    url(r'^negative/', dashboard_views.neg, name='negative'),
    url(r'^sentiment/', dashboard_views.sentiment, name='sentiment'),
    url(r'^api/in_t/$', dashboard_views.Elements_list_t, name='api_in_t'),
    url(r'^api/in_e/$', dashboard_views.Elements_list_e, name='api_in_e'),
    url(r'^api/resource/(?P<typeof>[\u4e00-\u9fa5]+)$', dashboard_views.negative_resource, name='resource'),
    url(r'^api/sentiment/$', dashboard_views.Sentiment_list, name='sentiment_list'),
    url(r'^api/negative/$', dashboard_views.Negative_list, name='negative_list'),
    url(r'^api/negtotal/$', dashboard_views.Neg_total, name='negative_total'),
]
