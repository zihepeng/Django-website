from django.urls import path
from index import views
urlpatterns = [
    path('about-us/', views.home),
    path('about-us/movies/', views.movies_select_all, name="movies_select_all"),
    path('movies_delete/', views.movies_delete, name='movies_delete'),
    path('movies_insert/', views.movies_insert, name='movies_insert'),
    path('movies_insert_handler/', views.movies_insert_handler, name='movies_insert_handler'),
    path('search/', views.search, name='search'),

]

