from django.urls import path
from basic_app import views

# For URL TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('mother/',views.mother,name='mother')
]