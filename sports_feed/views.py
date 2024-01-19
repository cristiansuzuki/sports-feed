from django.shortcuts import render
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats import endpoints
from datetime import timedelta, datetime, date
# Create your views here.


def index(request):
    data_pontos = endpoints.leagueleaders.LeagueLeaders(
        season=SeasonAll.current_season, per_mode48='PerGame')
        # aqui é feito uma consulta no Endpoint da nba-api, trazendo os líderes da temporada REGULAR e armazenando em uma variável

    df_pontos = data_pontos.league_leaders.get_data_frame()
    # o Pandas aqui trata os dados que foram pegados da API

    jogador = (df_pontos.PLAYER[0], df_pontos.PTS[0])
    jogador1 = (df_pontos.PLAYER[1], df_pontos.PTS[1])
    jogador2 = (df_pontos.PLAYER[2], df_pontos.PTS[2])
    jogador3 = (df_pontos.PLAYER[3], df_pontos.PTS[3])
    jogador4 = (df_pontos.PLAYER[4], df_pontos.PTS[4])

    print('JOGADOR COM MAIOR MEDIA DE PONTOS: ', jogador)

    return render(request, 'index.html', {'jogador': jogador, 'jogador1': jogador1,'jogador2': jogador2,'jogador3': jogador3,'jogador4': jogador4})