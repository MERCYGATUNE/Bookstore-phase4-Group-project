"""Add image to Book model

Revision ID: 14dec3d5ea6a
Revises: d3127551af83
Create Date: 2024-07-19 01:26:13.837190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14dec3d5ea6a'
down_revision = 'd3127551af83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
    #batch_op.add_column(sa.Column('image', sa.String(length=255), nullable=True))

     with op.batch_alter_table('borrowed_books', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('return_date',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrowed_books', schema=None) as batch_op:
        batch_op.alter_column('return_date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###