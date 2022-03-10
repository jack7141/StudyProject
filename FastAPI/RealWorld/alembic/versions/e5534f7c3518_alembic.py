"""alembic

Revision ID: e5534f7c3518
Revises: 
Create Date: 2022-02-23 18:30:07.468246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5534f7c3518'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer, primary_key=True),
        # 다른 손님과 식별 위한 고유키 id
        sa.Column('firstname', sa.String(50), nullable=False),
        # 이름
        sa.Column('lastname', sa.String(50), nullable=False),
        # 성
        sa.Column('recentvisit', sa.DateTime)
        # 최근 방문일자
    )


def downgrade():
    op.drop_table('customer')
