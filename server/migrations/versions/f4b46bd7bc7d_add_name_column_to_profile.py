"""Add name column to profile

Revision ID: f4b46bd7bc7d
Revises: d91629c3baf9
Create Date: 2024-07-17 08:41:31.367487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4b46bd7bc7d'
down_revision = 'd91629c3baf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
