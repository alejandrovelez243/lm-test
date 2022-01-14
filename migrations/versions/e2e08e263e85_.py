"""empty message

Revision ID: e2e08e263e85
Revises: 2454da000b2e
Create Date: 2022-01-14 15:10:11.959856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2e08e263e85'
down_revision = '2454da000b2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_password_key', 'user', type_='unique')
    op.drop_constraint('user_username_key', 'user', type_='unique')
    op.drop_column('user', 'password')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    op.create_unique_constraint('user_password_key', 'user', ['password'])
    # ### end Alembic commands ###