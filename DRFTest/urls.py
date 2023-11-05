from django.urls import path, include
from DRFTest import views


urlpatterns = [
    path('publisher/', views.PublisherList.as_view(), name='PublisherList'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='PublisherDetail')
]
