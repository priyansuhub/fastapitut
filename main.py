from fastapi import FastAPI

app = FastAPI()

#Path operation
@app.get('/')
async def root():
    return {"message":"Hola"}