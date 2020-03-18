from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<pk>/', views.SchoolDetailView.as_view(), name='detail'),
]
