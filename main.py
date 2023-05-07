# Import FastAPI class
from fastapi import FastAPI 
from fastapi.params import Body 


# Create instance of fast api class. 
app = FastAPI()   

 
#  Create path operation or route using http get method
@app.get("/")
async def root():
    """ Routes which show simple message."""
    return {"message":"Created first path operation using fast api"}

@app.get("/show-post")
async def show_message():
    """ Routes which show simple message using /show-post ."""
    return {"message":"Created /show-post path operation using fast api"}


# Create route using http post
@app.post("/create-post")
async def create_Post():
    """ Create a post using http post.
    """
    return {"message": "Successfully created post. "}

# get post data from body
@app.post("/create-post-from-body")
def Create_post_from_body(payload: dict = Body(...)):
    """ Create a post using http post and return the data from body.
    """
    return {"data":payload,"message": "Successfully created post. "}


