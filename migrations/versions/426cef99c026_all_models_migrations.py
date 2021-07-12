"""all models migrations

Revision ID: 426cef99c026
Revises: 4cad96b74ef3
Create Date: 2021-07-10 17:08:58.298372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '426cef99c026'
down_revision = '4cad96b74ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('preco', sa.DECIMAL(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('produtos')
    op.drop_constraint('conta_produto_id_produto_fkey', 'conta_produto', type_='foreignkey')
    op.create_foreign_key(None, 'conta_produto', 'produtos', ['id_produto'], ['id'])
    op.drop_constraint('estoque_produto_id_produto_fkey', 'estoque_produto', type_='foreignkey')
    op.create_foreign_key(None, 'estoque_produto', 'produtos', ['id_produto'], ['id'])
    op.drop_constraint('fornecedor_produto_id_produto_fkey', 'fornecedor_produto', type_='foreignkey')
    op.create_foreign_key(None, 'fornecedor_produto', 'produtos', ['id_produto'], ['id'])
    op.drop_constraint('produto_ordem_de_compra_id_produto_fkey', 'produto_ordem_de_compra', type_='foreignkey')
    op.create_foreign_key(None, 'produto_ordem_de_compra', 'produtos', ['id_produto'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'produto_ordem_de_compra', type_='foreignkey')
    op.create_foreign_key('produto_ordem_de_compra_id_produto_fkey', 'produto_ordem_de_compra', 'produto', ['id_produto'], ['id'])
    op.drop_constraint(None, 'fornecedor_produto', type_='foreignkey')
    op.create_foreign_key('fornecedor_produto_id_produto_fkey', 'fornecedor_produto', 'produto', ['id_produto'], ['id'])
    op.drop_constraint(None, 'estoque_produto', type_='foreignkey')
    op.create_foreign_key('estoque_produto_id_produto_fkey', 'estoque_produto', 'produto', ['id_produto'], ['id'])
    op.drop_constraint(None, 'conta_produto', type_='foreignkey')
    op.create_foreign_key('conta_produto_id_produto_fkey', 'conta_produto', 'produto', ['id_produto'], ['id'])
    op.create_table('produto',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('descricao', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('preco', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='produto_pkey')
    )
    op.drop_table('produtos')
    # ### end Alembic commands ###
