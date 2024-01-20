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
    data_pontos = endpoints.leagueleaders.LeagueLeaders(season=SeasonAll.current_season, per_mode48='PerGame')
        # aqui é feito uma consulta no Endpoint da nba-api, trazendo os líderes em PONTOS da TEMPORADA REGULAR e armazenando em uma variável 

    df_pontos = data_pontos.league_leaders.get_data_frame()
    # o Pandas aqui trata os dados que foram pegados da API

    jogador = (df_pontos.PLAYER[0], df_pontos.PTS[0])
    jogador1 = (df_pontos.PLAYER[1], df_pontos.PTS[1])
    jogador2 = (df_pontos.PLAYER[2], df_pontos.PTS[2])
    jogador3 = (df_pontos.PLAYER[3], df_pontos.PTS[3])
    jogador4 = (df_pontos.PLAYER[4], df_pontos.PTS[4])
    # nesse bloco acima, armazenei as variáveis relacionadas as suas respectivas posições dos jogadores

    # esse bloco abaixo segue a mesma ideia, so que para rebotes ao inves de pontos
    data_rebotes = endpoints.leagueleaders.LeagueLeaders(season=SeasonAll.current_season, stat_category_abbreviation='REB', per_mode48='PerGame')
    df_rebotes = data_rebotes.league_leaders.get_data_frame()

    jogador_reb = (df_rebotes.PLAYER[0], df_rebotes.REB[0])
    jogador_reb1 = (df_rebotes.PLAYER[1], df_rebotes.REB[1])
    jogador_reb2 = (df_rebotes.PLAYER[2], df_rebotes.REB[2])
    jogador_reb3 = (df_rebotes.PLAYER[3], df_rebotes.REB[3])
    jogador_reb4 = (df_rebotes.PLAYER[4], df_rebotes.REB[4])

    # assistencias
    data_assistencias = endpoints.leagueleaders.LeagueLeaders(season=SeasonAll.current_season, stat_category_abbreviation='AST', per_mode48='PerGame')
    df_assistencias = data_assistencias.league_leaders.get_data_frame()

    jogador_assist = (df_assistencias.PLAYER[0], df_assistencias.AST[0])
    jogador_assist1 = (df_assistencias.PLAYER[1], df_assistencias.AST[1])
    jogador_assist2 = (df_assistencias.PLAYER[2], df_assistencias.AST[2])
    jogador_assist3 = (df_assistencias.PLAYER[3], df_assistencias.AST[3])
    jogador_assist4 = (df_assistencias.PLAYER[4], df_assistencias.AST[4])

    return render(request, 'index.html', {'jogador': jogador, 'jogador1': jogador1,'jogador2': jogador2,'jogador3': jogador3,'jogador4': jogador4,
    'jogador_reb':jogador_reb, 'jogador_reb1':jogador_reb1, 'jogador_reb2':jogador_reb2, 'jogador_reb3':jogador_reb3, 'jogador_reb4':jogador_reb4, 
    'jogador_assist': jogador_assist, 'jogador_assist1': jogador_assist1, 'jogador_assist2': jogador_assist2, 'jogador_assist3': jogador_assist3, 'jogador_assist4': jogador_assist4, 
    })