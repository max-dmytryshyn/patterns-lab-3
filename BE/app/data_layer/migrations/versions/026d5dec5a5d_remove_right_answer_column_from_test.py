"""Remove right answer column from Test

Revision ID: 026d5dec5a5d
Revises: b1e2cba9133d
Create Date: 2023-04-26 23:01:01.504482

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '026d5dec5a5d'
down_revision = 'b1e2cba9133d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_column('right_answer')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('right_answer', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
