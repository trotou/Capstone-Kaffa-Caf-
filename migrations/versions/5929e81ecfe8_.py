"""empty message

Revision ID: 5929e81ecfe8
Revises: 
Create Date: 2021-07-09 15:19:38.312781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5929e81ecfe8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caixas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('valor_inicial', sa.Float(), nullable=True),
    sa.Column('saldo', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forma_pagamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('garcons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mesas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operadores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('id_caixa', sa.Integer(), nullable=False),
    sa.Column('id_garcom', sa.Integer(), nullable=False),
    sa.Column('id_mesa', sa.Integer(), nullable=False),
    sa.Column('id_forma_pagamento', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_caixa'], ['caixas.id'], ),
    sa.ForeignKeyConstraint(['id_forma_pagamento'], ['forma_pagamento.id'], ),
    sa.ForeignKeyConstraint(['id_garcom'], ['garcons.id'], ),
    sa.ForeignKeyConstraint(['id_mesa'], ['mesas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operador_caixa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_operador', sa.Integer(), nullable=False),
    sa.Column('id_caixa', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_caixa'], ['caixas.id'], ),
    sa.ForeignKeyConstraint(['id_operador'], ['operadores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_caixa'),
    sa.UniqueConstraint('id_operador')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operador_caixa')
    op.drop_table('contas')
    op.drop_table('operadores')
    op.drop_table('mesas')
    op.drop_table('garcons')
    op.drop_table('forma_pagamento')
    op.drop_table('caixas')
    # ### end Alembic commands ###
