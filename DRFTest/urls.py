from django.urls import path, include
from DRFTest import views


urlpatterns = [
    path('publisher/', views.PublisherList.as_view(), name='PublisherList'),
    path('publisher/<slug:slug>/', views.PublisherDetail.as_view(), name='PublisherDetail'),
    path('category/', views.CategoryList.as_view(), name='CategoryList'),
    path('category/<slug:slug>', views.CategoryDetail.as_view(), name='CategoryDetail'),
    path('author/', views.AuthorList.as_view(), name='AuthorList'),
    path('author/<slug:slug>', views.AuthorDetail.as_view(), name='AuthorDetail'),
    path('book/', views.BookList.as_view(), name='BookList'),
    path('book/<slug:slug>', views.BookDetail.as_view(), name='BookDetail'),
]
