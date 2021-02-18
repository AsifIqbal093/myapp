from django.urls import path

from . import  views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.details, name='detail'),
    path('<int:question_id/result/', views.results, name='result'),
    path('<int:question_id/vote/', views.vote, name='vote'),
]

