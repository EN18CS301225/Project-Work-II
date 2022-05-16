from django.urls import path
from . import views

app_name="entry"

urlpatterns = [
    path('', views.gratitude, name='gratitude'),
    path('entry/', views.entry, name='entry'),
    path('entry/show/', views.show, name='show'),
    path('show/<int:diary_id>', views.detail, name='detail'),
    path('productivity/', views.productivity, name='productivity'),
]