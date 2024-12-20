"""empty message

Revision ID: a03c8bb5966f
Revises: 3305e4ddfa9c
Create Date: 2020-01-27 17:48:59.715600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03c8bb5966f'
down_revision = '3305e4ddfa9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('no', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=16), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('modeldata', sa.String(length=128), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('file', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('no'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('pw', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('model')
    # ### end Alembic commands ###
