"""empty message

Revision ID: 663518bb62be
Revises: 51f5ccfba190
Create Date: 2021-09-04 11:16:55.945335

"""

# revision identifiers, used by Alembic.
revision = '663518bb62be'
down_revision = '51f5ccfba190'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boxes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('koda_izdelka', sa.String(length=64), nullable=True),
    sa.Column('opombe', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_boxes_koda_izdelka'), 'boxes', ['koda_izdelka'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_boxes_koda_izdelka'), table_name='boxes')
    op.drop_table('boxes')
    # ### end Alembic commands ###
