"""data

Revision ID: 184d9247c8ed
Revises: 44351d55ea2b
Create Date: 2024-12-21 18:48:41.186911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '184d9247c8ed'
down_revision: Union[str, None] = '44351d55ea2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO users ( name, email)
        VALUES
            ('Batova Ekaterina', 'ek@mail.ru'),
            ('Gluchov Ilya', 'ilya@mail.ru'),
            ('Alsia Mimimi', 'alice@mail.ru');
        """
    )

    op.execute(
        """
        INSERT INTO subscriptions (name, price, is_active, expires_at, auto_renew)
        VALUES
            ('Standart 30', 9.99, TRUE, NOW() + interval '30 days', FALSE),
            ('Standart 60', 19.99, TRUE, NOW() + interval '60 days', TRUE),
            ('Standart 365', 99.99, TRUE, NOW() + interval '365 days', TRUE);
        """
    )

    op.execute(
        """
        INSERT INTO payment_methods (user_id, card_number, expiry_date, balance, cvv, is_default)
        VALUES
            (1, '1111222233334444', '12/23', 100.0, '195', TRUE),
            (2, '5555666677778888', '06/32', 200.0, '182', TRUE),
            (3, '9999000011112222', '01/25', 300.0, '983', TRUE);
        """
    )

    op.execute(
        """
        INSERT INTO payments (user_id, subscription_id, amount, created_at)
        VALUES
            (1, 1, 10, NOW()),
            (2, 2, 12, NOW() - interval '15 days'),
            (3, 3, 11, NOW() - interval '30 days');
        """
    )

    op.execute(
        """
        INSERT INTO notifications (user_id, message, created_at)
        VALUES
            (1, 'Уведомление №1', NOW()),
            (2, 'Уведомление №2', NOW()),
            (3, 'Уведомление №3', NOW());
        """
    )


def downgrade():
    op.execute("DELETE FROM notifications;")
    op.execute("DELETE FROM payments;")
    op.execute("DELETE FROM payment_methods;")
    op.execute("DELETE FROM subscriptions;")
    op.execute("DELETE FROM users;")