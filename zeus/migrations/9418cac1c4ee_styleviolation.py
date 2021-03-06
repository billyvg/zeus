"""styleviolation

Revision ID: 9418cac1c4ee
Revises: 890ddf764ed7
Create Date: 2017-11-16 12:51:29.554079

"""
from alembic import op
import sqlalchemy as sa

import zeus


# revision identifiers, used by Alembic.
revision = "9418cac1c4ee"
down_revision = "890ddf764ed7"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "styleviolation",
        sa.Column("job_id", zeus.db.types.guid.GUID(), nullable=False),
        sa.Column("filename", sa.Text(), nullable=False),
        sa.Column("severity", zeus.db.types.enum.Enum(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("lineno", sa.Integer(), nullable=True),
        sa.Column("colno", sa.Integer(), nullable=True),
        sa.Column("source", sa.Text(), nullable=True),
        sa.Column("repository_id", zeus.db.types.guid.GUID(), nullable=False),
        sa.Column("id", zeus.db.types.guid.GUID(), nullable=False),
        sa.Column(
            "date_created",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["job_id"], ["job.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["repository_id"], ["repository.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_styleviolation_repository_id"),
        "styleviolation",
        ["repository_id"],
        unique=False,
    )


# ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_styleviolation_repository_id"), table_name="styleviolation")
    op.drop_table("styleviolation")


# ### end Alembic commands ###
