"""empty message

Revision ID: eb95d67df41f
Revises: ee3eb85cebee
Create Date: 2020-02-02 19:53:32.079263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb95d67df41f'
down_revision = 'ee3eb85cebee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('no', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
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
