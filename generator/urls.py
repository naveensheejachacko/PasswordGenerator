from django.urls import path
from . import  views
urlpatterns = [
    path('',views.home,name = "home"),
    path('listall',views.listall,name='listall'),
    path('delete/<int:id>',views.deleteRecord,name = "deleteRecord"),
    path('search',views.search,name = 'search'),
]