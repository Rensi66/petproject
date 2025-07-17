from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name = 'welcome'),
    path('about/', about, name = 'about'),
    path('menu/', menu, name='menu'),
    path('menu/<str:category>/', menu, name='chs_dsh'),
    path('reservation/', callback_view, name='reservation'),
]