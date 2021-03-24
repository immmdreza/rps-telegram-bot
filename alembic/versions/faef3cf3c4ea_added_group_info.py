"""Added Group Info

Revision ID: faef3cf3c4ea
Revises: 34fec86cdf69
Create Date: 2021-03-24 02:35:56.932053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faef3cf3c4ea'
down_revision = '34fec86cdf69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'group_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('creator', sa.Integer(), nullable=False),
        sa.Column('admins', sa.JSON(), nullable=True),
        sa.Column('first_join_date', sa.DateTime(), nullable=True),
        sa.Column('last_join_date', sa.DateTime(), nullable=True),
        sa.Column('games_count', sa.Integer(), nullable=False),
        sa.Column('last_game_date', sa.DateTime(), nullable=True),
        sa.Column('maximum_players', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_info')
    # ### end Alembic commands ###
