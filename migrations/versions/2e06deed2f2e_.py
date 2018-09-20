"""empty message

Revision ID: 2e06deed2f2e
Revises: 
Create Date: 2018-09-20 11:14:25.466945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e06deed2f2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hellos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hello', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hellos')
    # ### end Alembic commands ###