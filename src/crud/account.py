# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy import update
# from src.models.models import Account
# from datetime import datetime

# async def create_account(db: AsyncSession, user_id: int, balance: float):
#     account = Account(user_id=user_id, balance=balance)
#     db.add(account)
#     await db.commit()
#     await db.refresh(account)
#     return account

# async def get_account(db: AsyncSession, account_id: int):
#     result = await db.execute(select(Account).filter(Account.id == account_id))
#     return result.scalars().first()

# async def update_account_balance(db: AsyncSession, account_id: int, amount: float):
#     query = update(Account).where(Account.id == account_id).values(balance=amount, last_updated=datetime.now())
#     await db.execute(query)
#     await db.commit()
