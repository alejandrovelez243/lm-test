"""empty message

Revision ID: f56e1d09eabe
Revises: 1675887d5bf3
Create Date: 2022-01-14 17:44:25.035592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f56e1d09eabe'
down_revision = '1675887d5bf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('state_fullname', sa.String(length=40), nullable=True))
    op.drop_column('user', 'state_fullname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('state_fullname', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    op.drop_column('city', 'state_fullname')
    # ### end Alembic commands ###
