import requests
import os
from .models import Player, Team, PlayerStats, PlayerMatchHistory, db

RIOT_API_KEY = os.getenv('RGAPI-56b9ca76-f7e8-4264-82dd-da98c19d085c')

# Função para buscar as informações de um jogador
def get_player_info(player_id):
    url = f"https://api.riotgames.com/lol/summoner/v4/summoners/{player_id}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

# Função para buscar as estatísticas de um jogador
def get_player_stats(player_id):
    url = f"https://api.riotgames.com/lol/league/v4/entries/by-account/{player_id}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

# Função para buscar o histórico de partidas do jogador
def get_player_match_history(player_id):
    url = f"https://api.riotgames.com/lol/match/v4/matchlists/by-account/{player_id}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

# Função para armazenar as informações do jogador no banco
def store_player_info(player_data, team_id):
    player = Player.query.filter_by(id=player_data['id']).first()
    if not player:
        player = Player(
            id=player_data['id'],
            name=player_data['name'],
            team_id=team_id
        )
        db.session.add(player)
        db.session.commit()
    
    return player

# Função para armazenar as estatísticas do jogador no banco
def store_player_stats(player_stats_data, player_id):
    stats = PlayerStats.query.filter_by(player_id=player_id).first()
    if not stats:
        stats = PlayerStats(
            player_id=player_id,
            rank=player_stats_data[0].get('tier', 'Unranked'),
            wins=player_stats_data[0].get('wins', 0),
            losses=player_stats_data[0].get('losses', 0),
            points=player_stats_data[0].get('leaguePoints', 0)
        )
        db.session.add(stats)
        db.session.commit()

# Função para armazenar o histórico de partidas do jogador no banco
def store_player_match_history(match_history_data, player_id):
    for match in match_history_data['matches']:
        match_record = PlayerMatchHistory(
            player_id=player_id,
            match_id=match['gameId']
        )
        db.session.add(match_record)
    db.session.commit()

# Função para atualizar todos os dados de um jogador
def update_player_data(player_id, team_id):
    player_info = get_player_info(player_id)
    player_stats = get_player_stats(player_id)
    player_match_history = get_player_match_history(player_id)

    player = store_player_info(player_info, team_id)
    store_player_stats(player_stats, player.id)
    store_player_match_history(player_match_history, player.id)

# Função para atualizar os times de uma liga
def update_teams_in_league(league_id):
    url = f"https://api.riotgames.com/lol/leagues/v4/entries/{league_id}/teams"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        teams_data = response.json()
        for team_data in teams_data:
            team = Team.query.filter_by(name=team_data['name']).first()
            if not team:
                team = Team(
                    name=team_data['name']
                )
                db.session.add(team)
                db.session.commit()

                # Adicionar jogadores a cada time
                for player_data in team_data['players']:
                    store_player_info(player_data, team.id)
        
        db.session.commit()
    else:
        print(f"Erro ao atualizar times da liga {league_id}: {response.status_code}")
