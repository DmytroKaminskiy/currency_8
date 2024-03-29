"""Added required tables

Revision ID: f761383f4414
Revises: 
Create Date: 2022-11-07 18:01:44.319362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f761383f4414'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zoom_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=120), nullable=True),
    sa.Column('payload', sa.JSON(), nullable=True),
    sa.Column('event_ts', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zoom_event_event'), 'zoom_event', ['event'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_zoom_event_event'), table_name='zoom_event')
    op.drop_table('zoom_event')
    # ### end Alembic commands ###
