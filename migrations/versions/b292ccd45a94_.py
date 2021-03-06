"""empty message

Revision ID: b292ccd45a94
Revises: 7dee43f1b39f
Create Date: 2021-09-04 12:22:26.844379

"""

# revision identifiers, used by Alembic.
revision = 'b292ccd45a94'
down_revision = '7dee43f1b39f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boxes', sa.Column('nalog', sa.String(length=64), nullable=True))
    op.drop_index('ix_boxes_koda_izdelka', table_name='boxes')
    op.create_index(op.f('ix_boxes_koda_izdelka'), 'boxes', ['koda_izdelka'], unique=False)
    op.create_index(op.f('ix_boxes_nalog'), 'boxes', ['nalog'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_boxes_nalog'), table_name='boxes')
    op.drop_index(op.f('ix_boxes_koda_izdelka'), table_name='boxes')
    op.create_index('ix_boxes_koda_izdelka', 'boxes', ['koda_izdelka'], unique=False)
    op.drop_column('boxes', 'nalog')
    # ### end Alembic commands ###
