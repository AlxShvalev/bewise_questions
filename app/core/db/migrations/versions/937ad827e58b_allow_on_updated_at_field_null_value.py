"""Allow on updated_at field Null value

Revision ID: 937ad827e58b
Revises: d6be3d0699bf
Create Date: 2023-05-29 16:07:47.602865

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '937ad827e58b'
down_revision = 'd6be3d0699bf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questions', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questions', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
