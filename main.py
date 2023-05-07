# Import FastAPI class
from fastapi import FastAPI 


# Create instance of fast api class. 
app = FastAPI()   

 
#  Create path operation or route using http method
@app.get("/")
async def root():
    """ Routes which show simple message."""
    return {"message":"Created first path operation using fast api"}

@app.get("/show-message")
async def show_message():
    """ Routes which show simple message using /show ."""
    return {"message":"Created /show-message path operation using fast api"}
