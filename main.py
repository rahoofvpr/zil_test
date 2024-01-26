from fastapi import FastAPI
from schemas.expense import Expense as ExpenseSchema
from models.expense import Expense as ExpenseModel
from service.expense import Expense as ExpenseService
from sqlalchemy.orm import Session
app = FastAPI()
    
@app.post("/expenses/")
async def create_expenses(expense : ExpenseSchema):
    """
    this function to create new expense
    """
    ins_expense = ExpenseModel(name=expense.name,amount=expense.amount,category=expense.category)
    return ExpenseService.create_expense(ins_expense,Session)



