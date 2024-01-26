from pydantic import BaseModel

class Expense(BaseModel):
    name: str
    amount: float = 0.0
    category: str | None = None