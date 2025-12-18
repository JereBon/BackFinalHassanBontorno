"""add password column to clients

Revision ID: 6425252b8110
Revises: 002_add_client_id
Create Date: 2025-12-14 03:57:41.055459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6425252b8110'
down_revision: Union[str, Sequence[str], None] = '002_add_client_id'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('clients', sa.Column('password', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('clients', 'password')
