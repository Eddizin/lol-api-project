from flask import Blueprint, jsonify
from .models import Player, Team, PlayerStats, PlayerMatchHistory
from .services import update_player_data, update_teams_in_league

bp = Blueprint('api', __name__)

# Rota para obter todos os jogadores
@bp.route('/players')
def get_players():
    players = Player.query.all()
    return jsonify([player.name for player in players])

# Rota para obter todos os times
@bp.route('/teams')
def get_teams():
    teams = Team.query.all()
    return jsonify([team.name for team in teams])

# Rota para obter todos os dados de um jogador
@bp.route('/player/<int:player_id>')
def get_player(player_id):
    player = Player.query.filter_by(id=player_id).first()
    stats = PlayerStats.query.filter_by(player_id=player_id).first()
    match_history = PlayerMatchHistory.query.filter_by(player_id=player_id).all()
    return jsonify({
        'player': player.name,
        'stats': {
            'rank': stats.rank,
            'wins': stats.wins,
            'losses': stats.losses,
            'points': stats.points
        },
        'match_history': [match.match_id for match in match_history]
    })

# Rota para atualizar os dados dos jogadores de um time
@bp.route('/update_team_players/<int:league_id>')
def update_team_players(league_id):
    update_teams_in_league(league_id)
    return jsonify({"status": "Team players updated!"})
