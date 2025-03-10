"""Criar tabelas do banco de dados

Revision ID: 49ea90d04287
Revises: 
Create Date: 2025-02-23 13:50:59.429793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ea90d04287'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_match_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('match_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.String(length=20), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.Column('losses', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('jogadores')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jogadores',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('elo', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='jogadores_pkey')
    )
    op.drop_table('player_stats')
    op.drop_table('player_match_history')
    op.drop_table('player')
    op.drop_table('team')
    # ### end Alembic commands ###
