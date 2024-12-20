from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view()),  
    path('books/get/<pk>/', views.BookDetailView.as_view()), 
    path('books/create/', views.BookCreateView.as_view()),  
    path('books/<pk>/update/', views.BookUpdateView.as_view()),
    path('books/<pk>/delete/', views.BookDeleteView.as_view()), 
    path('books/filter/title/<title>/', views.BookFilterTitleView.as_view()), 
    path('books/filter/author/<author>/', views.BookFilterAuthorView.as_view()), 
    path('books/filter/genre/<genre>/', views.BookFilterGenreView.as_view()),  
    path('books/filter/year/<year>/', views.BookFilterYearView.as_view()),  
]