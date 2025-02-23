from . import db

# Modelo de jogador
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team = db.relationship('Team', back_populates='players')
    stats = db.relationship('PlayerStats', back_populates='player', uselist=False)
    match_history = db.relationship('PlayerMatchHistory', back_populates='player')

# Modelo de time
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    players = db.relationship('Player', back_populates='team')

# Modelo de estatísticas do jogador
class PlayerStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    rank = db.Column(db.String(20))
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    points = db.Column(db.Integer)
    player = db.relationship('Player', back_populates='stats')

# Modelo de histórico de partidas
class PlayerMatchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    match_id = db.Column(db.String(50))
    player = db.relationship('Player', back_populates='match_history')
