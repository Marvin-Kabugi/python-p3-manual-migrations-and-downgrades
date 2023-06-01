"""Renaming students to scholars

Revision ID: ceed5b593a0e
Revises: 791279dd0760
Create Date: 2023-06-01 17:44:54.746854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceed5b593a0e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
