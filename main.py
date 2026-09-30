from fastapi import FastAPI,Path,Query,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Annotated,Literal
import json

app=FastAPI()

class ExpenseTracker(BaseModel):

    title: Annotated[str, Field(..., description="where money is spent")]
    amount: Annotated[int, Field(...,gt=0, description=" how much money you spent ")]
    date: Annotated[str, Field(..., description="when you spend money")]
    payment_method: Annotated[Literal["Cash","UPI","Card", "Net Banking"],Field(..., description="how you pay")]
    description: Annotated[str, Field(..., description="why you spent money")]



def load_data():
    with open ("expenses.json",'r') as f:
        data = json.load(f)

    return data
   
def save_data(data):
    with open("expenses.json",'w') as f:
        json.dump(data,f)

@app.get("/")
def home():
    return {"message : api is running"} 

@app.post("/create")
def create_expense(ExpenseTracker:ExpenseTracker):

    data= load_data()

    if data:
        new_id=max(map(int, data.keys())) + 1
    else:
        new_id=1

    expense_data=ExpenseTracker.model_dump()

    expense_data["id"]=new_id

    data[str(new_id)] = expense_data

    save_data(data)

    return expense_data

@app.get("/expenses")
def get_expenses():
    data= load_data()

    return data 

@app.get("/expenses/search")
def search_expenses(title:str):

    data =load_data()

    results=[]

    for expense in data.values():

        if title.lower() in expense["title"].lower():
            results.append(expense)

    return results


@app.get("/expenses/{id}")
def get_expense(id:int):

    data= load_data()

    if  str(id) not in data:
        raise HTTPException(status_code=404,detail="Expense id not found")
    else:
        return data[str(id)]


@app.put("/expenses/{id}")
def update_expense(id:int,ExpenseTracker:ExpenseTracker):
    data = load_data()

    if str(id) not in data:
        raise HTTPException(status_code=404,detail="expense not found")

    expense_data = ExpenseTracker.model_dump()

    expense_data["id"] = id

    data[str(id)] = expense_data

    save_data(data)

    return expense_data


@app.delete("/expenses/{id}")
def delete_expense(id:int):

    data=load_data()
    if str(id) not in data:
        raise HTTPException(status_code=404,detail="expense not found")

    del data[str(id)]

    save_data(data)

    return {"message": "Expense deleted successfully"}

