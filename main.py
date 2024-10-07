from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "this is your app"}

@app.get("/post")
def post():
    return {"message": "this is your post"}


@app.post("/createposts")
def create_post(foodfind: dict = Body(...)):
    print(foodfind)
    return{"new_find": f"title: {foodfind['title']}, content:{foodfind['content']}"}