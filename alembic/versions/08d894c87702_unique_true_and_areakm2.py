"""unique=True and areakm2

Revision ID: 08d894c87702
Revises: 
Create Date: 2023-08-12 05:47:41.999725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08d894c87702'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('States',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('abbreviation', sa.String(length=255), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('capital', sa.String(length=255), nullable=True),
    sa.Column('area', sa.Float(), nullable=True),
    sa.Column('area_in_Km', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Counties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('area', sa.Float(), nullable=True),
    sa.Column('state_name', sa.String(length=255), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['States.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('area', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('state_name', sa.String(length=255), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('county_name', sa.String(length=255), nullable=True),
    sa.Column('county_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['county_id'], ['Counties.id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['States.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Cities')
    op.drop_table('Counties')
    op.drop_table('States')
    # ### end Alembic commands ###
