from django.urls import path
from .views import HeroesCreateView, HeroesUpdateView, HeroesListView, HeroDeleteView, HeroDetailView
from .views import VillainsCreateView, VillainsDeleteView, VillainsDetailView, VillainsUpdateView, VillainsListView
from .views import SideListView, SideCreateView, SideDeleteView, SideDetailView, SideUpdateView
from .views import SearchHeroesListView

urlpatterns = [
    path('hero_list/', HeroesListView.as_view(), name='hero_list'),
    path('hero_detail/<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('hero_create/', HeroesCreateView.as_view(), name='hero_create'),
    path('hero_update/<int:pk>/', HeroesUpdateView.as_view(), name='hero_update'),
    path('hero_delete/<int:pk>/', HeroDeleteView.as_view(), name="hero_delete"),
    path('villains_list/', VillainsListView.as_view(), name='villains_list'),
    path('villains_detail/<int:pk>/', VillainsDetailView.as_view(), name='villains_detail'),
    path('villains_create/', VillainsCreateView.as_view(), name='villains_create'),
    path('villains_update/<int:pk>/', VillainsUpdateView.as_view(), name='villains_update'),
    path('villains_delete/<int:pk>/', VillainsDeleteView.as_view(), name="villains_delete"),
    path('side_list/', SideListView.as_view(), name='side_list'),
    path('side_detail/<int:pk>/', SideDetailView.as_view(), name='side_detail'),
    path('side_create/', SideCreateView.as_view(), name='side_create'),
    path('side_update/<int:pk>/', SideUpdateView.as_view(), name='side_update'),
    path('side_delete/<int:pk>/', SideDeleteView.as_view(), name="side_delete"),
    path('searchH/', SearchHeroesListView.as_view(), name='search_results'),

]