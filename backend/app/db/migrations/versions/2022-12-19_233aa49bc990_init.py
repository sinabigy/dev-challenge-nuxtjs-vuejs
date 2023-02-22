"""Init

Revision ID: 233aa49bc990
Revises: 
Create Date: 2022-12-19 11:20:48.996618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '233aa49bc990'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Employee_id'), 'Employee', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Employee_id'), table_name='Employee')
    op.drop_table('Employee')
    # ### end Alembic commands ###
