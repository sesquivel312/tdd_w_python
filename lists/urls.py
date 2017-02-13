"""
originally copied from superlists/urls.py
"""
from django.conf.urls import url
from lists import views

from django.contrib import admin

# urls to support various functions all start with /lists
# /<listid> (GET) << view list given listid
# /new (POST) << create new id
# /<listid>/add_item (POST) << add NEW item to EXISTING list


urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    # url(r'^admin/', include(admin.site.urls)),
    ]
