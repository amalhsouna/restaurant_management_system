"""Create migration

Revision ID: 4e788a59eabc
Revises: 60a272f4be98
Create Date: 2024-12-05 13:37:09.421140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e788a59eabc'
down_revision: Union[str, None] = '60a272f4be98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
