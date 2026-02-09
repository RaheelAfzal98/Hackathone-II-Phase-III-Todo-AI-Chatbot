"""Add conversation and message tables for AI chatbot

Revision ID: 0001
Revises:
Create Date: 2026-01-20 23:10:00.000000

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create conversation table
    op.create_table(
        'conversation',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create index for user_id in conversation table
    op.create_index(op.f('ix_conversation_user'), 'conversation', ['user_id'])

    # Create message table
    op.create_table(
        'message',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('conversation_id', sa.Integer(), nullable=False),
        sa.Column('sender', sa.String(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.Column('tool_calls', sa.JSON(), nullable=True),
        sa.Column('tool_responses', sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create index for conversation_id in message table
    op.create_index(op.f('ix_message_conversation_id'), 'message', ['conversation_id'])


def downgrade() -> None:
    # Drop message table first (due to foreign key constraint)
    op.drop_index(op.f('ix_message_conversation_id'), table_name='message')
    op.drop_table('message')

    # Drop conversation table
    op.drop_index(op.f('ix_conversation_user'), table_name='conversation')
    op.drop_table('conversation')