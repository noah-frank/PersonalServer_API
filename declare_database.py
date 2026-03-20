import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

db = sa.create_engine("sqlite:///databases/stock_data.db")
Session = sessionmaker(bind=db)
Base = declarative_base()

class Ticker(base):
    __tablename__ = "Ticker"

    id: mapped[int] = mapped_column(primary_key=True)
    

# from sqlalchemy import select
# from sqlalchemy import MetaData, Table, Column, Integer, String, Float
# from sqlalchemy.types import DateTime

# metadata = MetaData()

# ticker_table = Table(
#     "TickerData", metadata,
#     Column("id", Integer, primary_key=True),
#     Column("datetime", DateTime, nullable=False),
#     Column("open", Float),
#     Column("")
# )