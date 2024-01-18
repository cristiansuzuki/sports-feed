from django.shortcuts import render
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats import endpoints
# Create your views here.


def index(request):
    data_pontos = endpoints.leagueleaders.LeagueLeaders(
        season=SeasonAll.current_season, per_mode48='PerGame')
    df_pontos = data_pontos.league_leaders.get_data_frame()
    jogador = (df_pontos.PLAYER[2])

    print('JOGADOR COM MAIOR MEDIA DE PONTOS: ', jogador)

    return render(request, 'index.html', {jogador: 'jogador'})