from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first_function():
    print("Hello wrold")
    return {"name":"sunny"}

@app.get("/id/{id}")
def second(id):
    return {"id":id}