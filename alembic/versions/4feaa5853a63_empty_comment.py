"""'empty comment.'

Revision ID: 4feaa5853a63
Revises: 5d96898673d9
Create Date: 2022-01-21 15:10:27.931204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4feaa5853a63'
down_revision = '5d96898673d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(length=2000), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_id'), 'file', ['id'], unique=False)
    op.create_index(op.f('ix_file_name'), 'file', ['name'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), server_default='', nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_id'), 'task', ['id'], unique=False)
    op.create_index(op.f('ix_task_title'), 'task', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_title'), table_name='task')
    op.drop_index(op.f('ix_task_id'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_file_name'), table_name='file')
    op.drop_index(op.f('ix_file_id'), table_name='file')
    op.drop_table('file')
    # ### end Alembic commands ###
