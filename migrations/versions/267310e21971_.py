"""empty message

Revision ID: 267310e21971
Revises: 07735f8d53c4
Create Date: 2021-09-04 22:24:07.944563

"""

# revision identifiers, used by Alembic.
revision = '267310e21971'
down_revision = '07735f8d53c4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boxes', sa.Column('tip', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('boxes', 'tip')
    # ### end Alembic commands ###
