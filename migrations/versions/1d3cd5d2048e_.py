"""empty message

Revision ID: 1d3cd5d2048e
Revises: af18ab028f09
Create Date: 2021-05-10 10:03:05.347296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d3cd5d2048e'
down_revision = 'af18ab028f09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
