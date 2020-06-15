"""add fullname

Revision ID: 02f4fccf9773
Revises: 3db586e9892a
Create Date: 2020-06-07 18:26:21.971654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02f4fccf9773'
down_revision = '3db586e9892a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###