
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_index,name='home'),
    path('stein/', home_steinbeck, name='stein'),
    path('post/', home_blog, name='blog'),
    path('post/<int:id>/', home_detail, name='detail'),
    path('grid/', home_grid, name='grid'),
    ]
