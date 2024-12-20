from rest_framework import filters
from .models import Book

class BookFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = request.GET.get('title')
        author = request.GET.get('author')
        genre = request.GET.get('genre')
        year = request.GET.get('year')  # Add year filter

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        if year:
            queryset = queryset.filter(year=year)  # Filter by year

        return queryset