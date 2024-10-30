from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None

class order(BaseModel):
    name: str
    order: str
    location: Optional[str]
    total: int


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

new_data = [{"name": "ali hussain", "order": "one large pizza", "location": "north nazimabad", "total": 1000, "id": 3}, {"name": "usman liaquat", "order": "beef burger with fries", "location": "gulshan e iqbal", "total": 1300, "id": 4}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def send_data(id):
    for p in new_data:
        if p["id"] == id:
            return p

@app.get("/")
def read_root():
    return{"message": "this is your app"}

@app.get("/posts")
def post():
    return {"data": my_posts}

@app.get("/data_check")
def data():
    return {"data": new_data}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return{"data": "post"}

@app.get("/posts/{id}")
def get_id(id: int):
    print(id)
    post = find_post(id)
    return {"post-message": post}

@app.post("/data_check")
def data_check(data: order):
    data_dict = data.dict()
    data_dict['id'] = randrange(0, 10000)
    new_data.append(data_dict)
    return {"client_data": "new data"} 


@app.get("/data_check/{id}")
def data_id(id: int):
    print(id)
    data = send_data(id)
    return {"post_message": data}
