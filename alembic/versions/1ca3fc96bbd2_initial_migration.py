"""Initial migration

Revision ID: 1ca3fc96bbd2
Revises: 
Create Date: 2023-05-02 14:57:14.174488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca3fc96bbd2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('bio', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_author_id'), 'author', ['id'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('summary', sa.String(length=250), nullable=True),
    sa.Column('publication_date', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.create_index(op.f('ix_book_summary'), 'book', ['summary'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_summary'), table_name='book')
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_author_id'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
