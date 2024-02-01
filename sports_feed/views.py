from django.shortcuts import render
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats import endpoints
from datetime import timedelta, datetime, date
from .models import *
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


    # roubos de bola
    data_steals = endpoints.leagueleaders.LeagueLeaders(season=SeasonAll.current_season, stat_category_abbreviation='STL', per_mode48='PerGame')
    df_steals = data_steals.league_leaders.get_data_frame()

    jogador_steal = (df_steals.PLAYER[0], df_steals.STL[0])
    jogador_steal1 = (df_steals.PLAYER[1], df_steals.STL[1])
    jogador_steal2 = (df_steals.PLAYER[2], df_steals.STL[2])
    jogador_steal3 = (df_steals.PLAYER[3], df_steals.STL[3])
    jogador_steal4 = (df_steals.PLAYER[4], df_steals.STL[4])

    # tocos
    data_tocos = endpoints.leagueleaders.LeagueLeaders(season=SeasonAll.current_season, stat_category_abbreviation='BLK', per_mode48='PerGame')
    df_tocos = data_tocos.league_leaders.get_data_frame()

    jogador_toco = (df_tocos.PLAYER[0], df_tocos.BLK[0])
    jogador_toco1 = (df_tocos.PLAYER[1], df_tocos.BLK[1])
    jogador_toco2 = (df_tocos.PLAYER[2], df_tocos.BLK[2])
    jogador_toco3 = (df_tocos.PLAYER[3], df_tocos.BLK[3])
    jogador_toco4 = (df_tocos.PLAYER[4], df_tocos.BLK[4])


    posts = Post.objects.all() #query set com todos os valores da Model post inclusos para serem exibidos na página inicial


    #função que irá criar um objeto com os dados tratados na Model
    def pontos():
        pontuadores = jogador, jogador1, jogador2, jogador3, jogador4
        valores_individuais = []

        for nome, pontuacao in pontuadores:
            valores_individuais.append(nome)
            valores_individuais.append(pontuacao)
        top = valores_individuais[0], valores_individuais[1], valores_individuais[2], valores_individuais[3], valores_individuais[4], valores_individuais[5]


        individual = ""

        for i in range(0, len(top), 2):
            individual += "{} {}\n".format(top[i], top[i + 1])
        
        print(individual)


        post_pontos = Post.objects.create(titulo='Lideres em Pontos Por Jogo', conteudo=individual)
        return post_pontos


    a = 1

    if a == 1:
        pontos()


    return render(request, 'index.html',{
    'jogador_reb':jogador_reb, 'jogador_reb1':jogador_reb1, 'jogador_reb2':jogador_reb2, 'jogador_reb3':jogador_reb3, 'jogador_reb4':jogador_reb4, 
    'jogador_assist': jogador_assist, 'jogador_assist1': jogador_assist1, 'jogador_assist2': jogador_assist2, 'jogador_assist3': jogador_assist3, 'jogador_assist4': jogador_assist4,
    'jogador_steal': jogador_steal, 'jogador_steal1': jogador_steal1, 'jogador_steal2': jogador_steal2, 'jogador_steal3': jogador_steal3, 'jogador_steal4': jogador_steal4, 
    'jogador_toco': jogador_toco, 'jogador_toco1': jogador_toco1, 'jogador_toco2': jogador_toco2, 'jogador_toco3': jogador_toco3, 'jogador_toco4': jogador_toco4,
    'posts': posts
    })