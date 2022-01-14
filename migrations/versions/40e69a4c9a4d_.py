"""empty message

Revision ID: 40e69a4c9a4d
Revises: e2e08e263e85
Create Date: 2022-01-14 15:30:25.063708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e69a4c9a4d'
down_revision = 'e2e08e263e85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('middle_name', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'middle_name')
    # ### end Alembic commands ###
