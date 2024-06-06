from alembic import op
import sqlalchemy as sa

revision = 'petsfoto'
down_revision = 'previous_revision'

def upgrade():
    op.add_column('animals', sa.Column('breed', sa.String(), nullable=True))
    op.add_column('animals', sa.Column('photo_url', sa.String(), nullable=True))

def downgrade():
    op.drop_column('animals', 'breed')
    op.drop_column('animals', 'photo_url')
