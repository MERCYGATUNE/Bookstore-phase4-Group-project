"""add title to class borrowed book

Revision ID: 1fc144707db6
Revises: c13a8dccc17c
Create Date: 2024-07-17 07:30:24.494771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc144707db6'
down_revision = 'c13a8dccc17c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrowed_books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrowed_books', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
