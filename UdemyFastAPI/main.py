from fastapi import FastAPI 
from fastapi import Body

app = FastAPI()

Books =[
    {'id':1, 'title':'title1', 'author':'author1'},
     {'id':2,'title':'title2', 'author':'author2'},
      {'id':3,'title':'title1', 'author':'author3'},
       {'id':4,'title':'title4', 'author':'author4'},
]
# b_oj= Books.objects.all(id = 2)
# create first path 
@app.get("/")
async def name():
    return {'message':"Created first end point"}


# return list of objects
@app.get("/book-list")
async def name():
    return {'data':Books}


# Path params :
#   req param attach to url
# find info based on loc
@app.get("/book_p/{id}")
async def get_book(id:int):
    return {'data':[book for book in Books if book["id"] == id]}


# Query params
# attached after ? 
# name=value pairs
@app.get("/book_q/")
async def get_books_by_queryParams(id:int):
    return {"data":[book for book in Books if book['id'] == id]}



# Path + query params
@app.get("/book_qp/{id}")
async def get_book(title:str,ids:int):
    return {'data':[book for book in Books if book['id'] == id or book['title'] == title]}


# Post 
# req  body to post data
@app.post("/book/create")
async def create_book(new_book = Body()):
    Books.append(new_book)
    return {'data':new_book}
    
# Put
# update data
@app.put("/book_update/{id}")
async def update_book(id:int, new_book=Body()):
    # for book in Books:
    #     if book['id'] == id:
    #         book.update(new_book)
    # return {'data':[book for book in Books if book["id"] == id]}
    [book.update(new_book) if book['id'] == id else book.update({'id': id*2}) for book in Books ]
    print("Books: ", Books)
    return {'data':[book for book in Books]}


# Delete
@app.delete("/book_delete/{id}")
async def delete_book(id:int):
    
    for book in Books:
        if book['id'] == id:
            Books.remove(book)
            return {"data": book}