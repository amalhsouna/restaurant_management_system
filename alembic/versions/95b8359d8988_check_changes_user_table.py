"""Check changes user table

Revision ID: 95b8359d8988
Revises: c4b94524ca0b
Create Date: 2024-12-06 14:45:39.313526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95b8359d8988'
down_revision: Union[str, None] = 'c4b94524ca0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('menus', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('orders', sa.Column('menu_id', sa.Integer(), nullable=True))
    op.drop_constraint('orders_user_id_fkey', 'orders', type_='foreignkey')
    op.drop_constraint('orders_dish_id_fkey', 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'menus', ['menu_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'orders', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('orders', 'dish_id')
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.add_column('orders', sa.Column('dish_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key('orders_dish_id_fkey', 'orders', 'menus', ['dish_id'], ['id'])
    op.create_foreign_key('orders_user_id_fkey', 'orders', 'users', ['user_id'], ['id'])
    op.drop_column('orders', 'menu_id')
    op.alter_column('menus', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###