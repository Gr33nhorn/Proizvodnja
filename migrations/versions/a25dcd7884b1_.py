"""empty message

Revision ID: a25dcd7884b1
Revises: bb03e5ac95a5
Create Date: 2021-09-15 19:44:47.027808

"""

# revision identifiers, used by Alembic.
revision = 'a25dcd7884b1'
down_revision = 'bb03e5ac95a5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nalogi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spremenjeno', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_nalogi_spremenjeno'), 'nalogi', ['spremenjeno'], unique=False)
    op.create_table('izdelki',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spremenjeno', sa.DateTime(), nullable=True),
    sa.Column('koda_izdelka', sa.String(length=64), nullable=True),
    sa.Column('nalogi', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['nalogi'], ['nalogi.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_izdelki_koda_izdelka'), 'izdelki', ['koda_izdelka'], unique=False)
    op.create_index(op.f('ix_izdelki_spremenjeno'), 'izdelki', ['spremenjeno'], unique=False)
    op.add_column('boxes', sa.Column('nalogi', sa.Integer(), nullable=True))
    op.add_column('boxes', sa.Column('izdelki', sa.Integer(), nullable=True))
    op.drop_index('ix_boxes_koda_izdelka', table_name='boxes')
    op.drop_index('ix_boxes_nalog', table_name='boxes')
    op.drop_index('ix_boxes_timestamp', table_name='boxes')
    op.create_foreign_key(None, 'boxes', 'izdelki', ['izdelki'], ['id'])
    op.create_foreign_key(None, 'boxes', 'nalogi', ['nalogi'], ['id'])
    op.drop_column('boxes', 'nalog')
    op.drop_column('boxes', 'timestamp')
    op.drop_column('boxes', 'koda_izdelka')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boxes', sa.Column('koda_izdelka', sa.VARCHAR(length=64), nullable=True))
    op.add_column('boxes', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.add_column('boxes', sa.Column('nalog', sa.VARCHAR(length=64), nullable=True))
    op.drop_constraint(None, 'boxes', type_='foreignkey')
    op.drop_constraint(None, 'boxes', type_='foreignkey')
    op.create_index('ix_boxes_timestamp', 'boxes', ['timestamp'], unique=False)
    op.create_index('ix_boxes_nalog', 'boxes', ['nalog'], unique=False)
    op.create_index('ix_boxes_koda_izdelka', 'boxes', ['koda_izdelka'], unique=False)
    op.drop_column('boxes', 'izdelki')
    op.drop_column('boxes', 'nalogi')
    op.drop_index(op.f('ix_izdelki_spremenjeno'), table_name='izdelki')
    op.drop_index(op.f('ix_izdelki_koda_izdelka'), table_name='izdelki')
    op.drop_table('izdelki')
    op.drop_index(op.f('ix_nalogi_spremenjeno'), table_name='nalogi')
    op.drop_table('nalogi')
    # ### end Alembic commands ###