from alembic import op
import sqlalchemy as sa

revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('senha', sa.String(length=250), nullable=False),
        sa.Column('role', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=70), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nome')
    )
    op.create_table(
        'pedidos',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('cliente_id', sa.Integer(), nullable=True),
        sa.Column('valor', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(['cliente_id'], ['usuarios.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('pedidos')
    op.drop_table('usuarios')
