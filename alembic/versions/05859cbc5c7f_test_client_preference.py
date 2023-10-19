"""test client_preference

Revision ID: 05859cbc5c7f
Revises: 769727ba0264
Create Date: 2023-10-15 00:15:30.224376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '05859cbc5c7f'
down_revision: Union[str, None] = '769727ba0264'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_preference',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_category', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_preference_id'), 'client_preference', ['id'], unique=False)
    op.alter_column('client', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('client', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('client', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('client', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_index(op.f('ix_client_preference_id'), table_name='client_preference')
    op.drop_table('client_preference')
    # ### end Alembic commands ###