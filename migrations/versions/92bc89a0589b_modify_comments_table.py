"""modify comments table

Revision ID: 92bc89a0589b
Revises: db7e04fd9e7e
Create Date: 2020-09-27 17:07:33.026325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92bc89a0589b'
down_revision = 'db7e04fd9e7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog', sa.Text(), nullable=True))
    op.drop_column('blogs', 'blog_content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_content', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('blogs', 'blog')
    # ### end Alembic commands ###