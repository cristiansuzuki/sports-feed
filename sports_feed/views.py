from django.shortcuts import render
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats import endpoints
from datetime import timedelta, datetime, date
import datetime
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
        #aqui guardei os dados, que na verdade são TUPLAS, dentro de uma variavel 
        pontuadores = jogador, jogador1, jogador2, jogador3, jogador4
        valores_individuais = []

        # o problema disso é que ficou uma TUPLA dentro de OUTRA TUPLA

        for nome, pontuacao in pontuadores:
            valores_individuais.append(nome)
            valores_individuais.append(pontuacao)
        dados_pontuadores = valores_individuais[0], valores_individuais[1], valores_individuais[2], valores_individuais[3], valores_individuais[4], valores_individuais[5], valores_individuais[6], valores_individuais[7], valores_individuais[8], valores_individuais[9]

        # a solução que encontrei foi percorrer um laço FOR e anexar essa tupla em um vetor usando a função APPEND
        # após isso criei outra variável com as posições dos vetores sendo adicionadas de forma separada

        # !!!! TALVEZ precise refatorar essa parte para evitar desperdício de código !!!!!

        # aqui criei uma variável com o nome individual que recebe uma string vazia, isso vai ser importante para transformar os dados do vetor em String

        individual_pts = ""
        
        # feito isso eu percorri outro laço For usando um Len para verificar o tamanho do vetor e formatei os dados para virarem STRING na variavel 'individual'

        for i in range(0, len(dados_pontuadores), 2):
            individual_pts += "{} {}\n".format(dados_pontuadores[i], dados_pontuadores[i + 1])
        
        # ao final de tudo, um objeto é criado no banco jogando um titulo fixo numa string, porém será incrementado Data e Hora posteriormente
        # o conteudo do POST também é inserido com os valores já tratados...toda vez que essa Função é chamada (assim que cumprir os requisitos) um novo Objeto é criado.
        post_pontos = Post.objects.create(titulo='Lideres em Pontos Por Jogo', conteudo=individual_pts)
        return post_pontos
    

    def rebotes():
        reboteiros = jogador_reb, jogador_reb1, jogador_reb2, jogador_reb3, jogador_reb4
        valores_reb = []

        for nome, valor in reboteiros:
            valores_reb.append(nome)
            valores_reb.append(valor)

        dados_reboteiros = valores_reb[0], valores_reb[1], valores_reb[2], valores_reb[3], valores_reb[4], valores_reb[5], valores_reb[6], valores_reb[7], valores_reb[8], valores_reb[9]

        individual_reb = ""

        for i in range(0, len(dados_reboteiros), 2):
            individual_reb += "{} {}\n".format(dados_reboteiros[i], dados_reboteiros[i + 1])
        
        post_rebotes = Post.objects.create(titulo='Lideres em Rebotes Por Jogo', conteudo=individual_reb)

        return post_rebotes
    
    def assistencias():
        assists = jogador_assist, jogador_assist1, jogador_assist2, jogador_assist3, jogador_assist4
        valores_assist = []

        for nome, valor in assists:
            valores_assist.append(nome)
            valores_assist.append(valor)
        
        dados_assists = valores_assist[0], valores_assist[1], valores_assist[2], valores_assist[3], valores_assist[4], valores_assist[5], valores_assist[6], valores_assist[7], valores_assist[8], valores_assist[9]

        individual_assist = ""

        for i in range(0, len(dados_assists), 2):
            individual_assist += "{} {}\n".format(dados_assists[i], dados_assists[i + 1])
        
        post_assistencias = Post.objects.create(titulo='Lideres em Assistências Por Jogo', conteudo=individual_assist)
        
        return post_assistencias
    
    def tocos():
        tocos = jogador_toco, jogador_toco1, jogador_toco2, jogador_toco3, jogador_toco4
        valores_tocos = []

        for nome, valor in tocos:
            valores_tocos.append(nome)
            valores_tocos.append(valor)
        
        dados_tocos = valores_tocos[0], valores_tocos[1], valores_tocos[2], valores_tocos[3], valores_tocos[4], valores_tocos[5], valores_tocos[6], valores_tocos[7], valores_tocos[8], valores_tocos[9]

        individual_tocos = ""

        for i in range(0, len(dados_tocos), 2):
            individual_tocos += "{} {}\n".format(dados_tocos[i], dados_tocos[i + 1])
        
        post_tocos = Post.objects.create(titulo='Lideres em Tocos Por Jogo', conteudo=individual_tocos)
        
        return post_tocos
    
    def steals():
        steals = jogador_steal, jogador_steal1, jogador_steal2, jogador_steal3, jogador_steal4
        valores_steals = []
        
        for nome, valor in steals:
            valores_steals.append(nome)
            valores_steals.append(valor)

        dados_steals = valores_steals[0], valores_steals[1], valores_steals[2], valores_steals[3], valores_steals[4], valores_steals[5], valores_steals[6], valores_steals[7], valores_steals[8], valores_steals[9]
        
        individual_steals = ""

        for i in range(0, len(dados_steals), 2):
            individual_steals += "{} {}\n".format(dados_steals[i], dados_steals[i + 1])
        
        post_steals = Post.objects.create(titulo='Lideres em Steals Por Jogo', conteudo=individual_steals)
        
        return post_steals
    
    
    # aqui sera inserido a verificação do dia da semana, dependendo do dia será chamada uma função semelhante a acima para ser criado um objeto e postado no Blog de forma automatica.
    
    dia = datetime.datetime.today()
    print("Dia da semana:" ,dia.weekday())

    if dia.weekday() == 0:
        pontos()
    
    if dia.weekday() == 1:
        rebotes()

    if dia.weekday() == 2:
        assistencias()

    if dia.weekday()==3:
        tocos()

    if dia.weekday()==4:
        steals()
    
    if dia.weekday() == 5:
        pass

    if dia.weekday() == 6:
        pass

    return render(request, 'index.html',{'posts': posts})