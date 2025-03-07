# Copyright 2018 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""adding background tasks table

Revision ID: 64d90a1a69bc
Revises: e5594ed3ab53
Create Date: 2022-06-12 20:00:38.183341

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "64d90a1a69bc"
down_revision = "e5594ed3ab53"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "background_tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("project", sa.String(length=255), nullable=False),
        sa.Column("created", sa.TIMESTAMP(), nullable=True),
        sa.Column("updated", sa.TIMESTAMP(), nullable=True),
        sa.Column("state", sa.String(length=255), nullable=True),
        sa.Column("timeout", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project", name="_background_tasks_uc"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("background_tasks")
    # ### end Alembic commands ###
