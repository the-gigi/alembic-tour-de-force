"""baseline

Revision ID: bc25b5f8939f
Revises:
Create Date: 2016-05-29 15:00:18.721577

"""

# revision identifiers, used by Alembic.
revision = 'bc25b5f8939f'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'bug',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('bug_tracker_url', sa.String(), nullable=False),
        sa.Column('root_cause', sa.String()),
        sa.Column('who', sa.String()),
        sa.Column('when', sa.DateTime(), default=sa.func.now()))


def downgrade():
    op.drop_table('bug')

