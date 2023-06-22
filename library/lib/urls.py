from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail')
]