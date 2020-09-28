"""roles out

Revision ID: 560d12227d7a
Revises: 601aa0f7c5dc
Create Date: 2020-09-28 12:00:55.593839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '560d12227d7a'
down_revision = '601aa0f7c5dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###