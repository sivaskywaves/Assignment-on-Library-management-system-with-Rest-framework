from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookFilterTitleView(APIView):
    def get(self, request, title):
        books = Book.objects.filter(title__icontains=title)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookFilterAuthorView(APIView):
    def get(self, request, author):
        books = Book.objects.filter(author__icontains=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookFilterGenreView(APIView):
    def get(self, request, genre):
        books = Book.objects.filter(genre__icontains=genre)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookFilterYearView(APIView):
    def get(self, request, year):
        books = Book.objects.filter(year=year)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)