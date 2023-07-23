# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
  

@app.get("/test")
async def root():
    return {"message": "Hello test"}

@app.get("/hello")
async def root():
    return {"message": "bye there"}

@app.get("/onemorequeryparameter")
async def root():
    return {"message": "here is one more"}