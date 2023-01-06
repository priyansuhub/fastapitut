from typing import Optional
from fastapi import  FastAPI,Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()
counter = 1



class Post(BaseModel):
    id: Optional[int] = -1
    title: str
    content: str
    publish: bool = True
    rating: Optional[int]=None

class Data(BaseModel):
    title: str
    content: str


my_posts = [{"id":1,"title":"Title of post 1", "content":"Content of post 1", "publish": False, "rating": 10}]

def indexExtractionByid(id):
    for i, p in enumerate(my_posts):
        if (p['id'] == id):
            print(type(i).__name__ , i)
            return i
    else:
        return  "Not found"

#Path operation
@app.get('/')
async def root():
    return {"message":"Hola"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(new_post: Post):
    global counter 
    counter+=1
    post_dict = new_post.dict()
    post_dict['id'] = counter
    my_posts.append(post_dict)
    return {"data":post_dict} 

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    data = ''
    for p in my_posts:
        print(p)
        if(p['id'] == id):
            data = p
            return p
    if data == '':
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"JNL{id} not found")
    
@app.delete("/posts/{id}")
def delete_data(id: int):
    data = indexExtractionByid(id)
    if(type(data).__name__ == "int"):
        my_posts.pop(data)
        raise HTTPException(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{data}")


@app.put("/posts/{id}")
def update_post(id:int, post_data:Data):
    data = indexExtractionByid(id)
    if(type(data).__name__ == "int"):
        #convert post_data to a dictionaly
        test_data = my_posts[data]
        test_data["title"] = post_data.title
        test_data["content"] = post_data.content
        my_posts[data] = test_data
        raise HTTPException(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{data}")
    

#title str, content str, category
