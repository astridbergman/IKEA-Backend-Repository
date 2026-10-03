from fastapi import FastAPI
from FairSource.routers import connection
from FairSource.routers import information

app = FastAPI()
app.include_router(connection.router)
app.include_router(information.router)

@app.get("/")
def read_root():
    return {"message": "IKEA Backend is running! SO IT WORKS"}