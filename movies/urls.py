from django.urls import path
from .views import FilmListView, FilmDeleteView, FilmUpdateView, FilmCreateView, FilmDetailView, AddComment

urlpatterns = [
    path('film_list/', FilmListView.as_view(), name='film_list'),
    path('film_detail/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('film_create/', FilmCreateView.as_view(), name='film_create'),
    path('film_update/<int:pk>/', FilmUpdateView.as_view(), name='film_update'),
    path('film_delete/<int:pk>/', FilmDeleteView.as_view(), name="film_delete"),
    path('film_comment/<int:pk>/', AddComment.as_view(), name='film_comment'),


]