from fastapi import FastAPI,Path,Query
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








