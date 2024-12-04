"""Create migration

Revision ID: 7f81b78614fd
Revises: 4e788a59eabc
Create Date: 2024-12-05 13:39:58.745234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f81b78614fd'
down_revision: Union[str, None] = '4e788a59eabc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
