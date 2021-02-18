from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('details/', include('polls.urls')),
    path('result/', include('polls.urls')),
    path('vote/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
