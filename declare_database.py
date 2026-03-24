import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, declarative_base, Session
from datetime import datetime

db = sa.create_engine("sqlite:///databases/stock_data.db", echo=True)
Base = declarative_base()

class Ticker(Base):
    __tablename__ = "Ticker"

    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[datetime]
    open: Mapped[float]
    high: Mapped[float]
    low: Mapped[float]
    close: Mapped[float]
    volume: Mapped[int]
    ticker: Mapped[str]
    SMA10: Mapped[float]
    SMA20: Mapped[float]
    SMA30: Mapped[float]
    AO: Mapped[float]
    ISA_9: Mapped[float]
    ISB_26: Mapped[float]
    ITS_9: Mapped[float]
    IKS_26: Mapped[float]

    def __repr__(self) -> str:
        return f"<id={self.id}, ticker={self.ticker}, datetime={self.datetime}, o={self.open}, h={self.high}, l={self.low}, c={self.close}"

def main() -> None:
    Base.metadata.create_all(db)
    with Session(db) as session:
        session.commit()
    
if __name__ == "__main__":
    main()
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