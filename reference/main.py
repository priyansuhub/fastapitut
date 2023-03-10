from typing import Optional
from fastapi import  FastAPI,Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', host='localhost', database='alt')
    cursor = cnx.cursor()
    print("connection successful")
except Exception as error:
    print("connection to database failed")



app = FastAPI()
counter = 1


class Post(BaseModel):
    title: str
    content: str
    published: bool = False

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
    cursor.execute("""SELECT * FROM mytable""")
    a = []
    b = {}
    key1 = "id"
    key2 = "title"
    key3 = "content"
    key4 = "published"
    key5 = "created_at"     
    for row in cursor:
        b[key1] = row[0]
        b[key2] = row[1]
        b[key3] = row[2]
        b[key4] = row[3]
        b[key5] = row[4]
        a.append(dict(b))
    print(a)
    return {"data": a}

@app.post("/posts")
def create_posts(new_post: Post):
    cursor.execute("""INSERT INTO mytable(title, content) VALUES (%s, %s)""",(new_post.title,new_post.content))
    new_post = cursor.fetchone()
    cnx.commit()
    return {"data": new_post}  

@app.get("/posts/{id}")
def get_post(id: int):
    query = "SELECT * from mytable WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    test_post = cursor.fetchone()
    print(test_post)
    return test_post
    #  data = ''
    # for p in my_posts:
    #     if(p['id'] == id):
    #         data = p
    #         return test_post
    # if data == '':
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"JNL{id} not found")
    
@app.delete("/posts/{id}")
def delete_data(id: int):
    cursor.execute("""DELETE FROM mytable WHERE id = %s""", (str(id),))
    


@app.put("/posts/{id}")
def update_post(id:int, post_data:Data):
    cursor.execute("""UPDATE mytable SET title = %s, content =%s, published = %s""",(post_data.title,post_data.content))
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
