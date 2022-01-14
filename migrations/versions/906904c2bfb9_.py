"""empty message

Revision ID: 906904c2bfb9
Revises: f56e1d09eabe
Create Date: 2022-01-14 17:45:05.860200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '906904c2bfb9'
down_revision = 'f56e1d09eabe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('latitu', sa.Float(precision=20), nullable=False))
    op.add_column('city', sa.Column('longitude', sa.Float(precision=20), nullable=False))
    op.drop_column('city', 'latitud')
    op.drop_column('city', 'longitud')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('longitud', sa.REAL(), autoincrement=False, nullable=False))
    op.add_column('city', sa.Column('latitud', sa.REAL(), autoincrement=False, nullable=False))
    op.drop_column('city', 'longitude')
    op.drop_column('city', 'latitu')
    # ### end Alembic commands ###