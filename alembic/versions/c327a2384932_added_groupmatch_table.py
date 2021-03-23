"""Added GroupMatch table

Revision ID: c327a2384932
Revises: 69b2d15ae0ce
Create Date: 2021-03-23 04:42:51.446603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c327a2384932'
down_revision = '69b2d15ae0ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'group_match',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('match_id', sa.String(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('creator', sa.Integer(), nullable=False),
        sa.Column('create_date', sa.DateTime(), nullable=False),
        sa.Column('finished', sa.Boolean(), nullable=False),
        sa.Column('players_status', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_match')
    # ### end Alembic commands ###
