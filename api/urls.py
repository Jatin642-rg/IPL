from django.urls import path
from .views import matches_per_year, matches_won_per_team

urlpatterns = [
    path('matches_per_year/', matches_per_year, name='matches_per_year'),
    path('matches_won_per_team/', matches_won_per_team, name='matches_won_per_team'),
]
