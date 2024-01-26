from sqlalchemy import Boolean, Column, Integer, String , Float

from utils.database import Base


class Expense(Base):
    __tablename__ = "tbl_expense"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    amount = Column(Float, default = 0.0)
    category = Column(Boolean, default=True)
    
    class Config:
        orm_mode = True