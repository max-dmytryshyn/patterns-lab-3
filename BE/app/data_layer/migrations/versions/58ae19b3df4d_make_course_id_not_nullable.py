"""Make course_id not nullable

Revision ID: 58ae19b3df4d
Revises: 0736a45999b8
Create Date: 2023-04-26 22:41:18.576912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ae19b3df4d'
down_revision = '0736a45999b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lection', schema=None) as batch_op:
        batch_op.alter_column('course_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.alter_column('course_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.alter_column('course_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('lection', schema=None) as batch_op:
        batch_op.alter_column('course_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###