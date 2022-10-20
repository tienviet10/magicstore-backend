from django.urls import path
from django.urls import re_path as url

from TicTacToe import views

urlpatterns = [
    url(r'^tictactoe$', views.tictactoe),
]
