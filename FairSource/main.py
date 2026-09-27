from fastapi import FastAPI
from FairSource.routers import connection

app = FastAPI()
app.include_router(connection.router)

@app.get("/")
def read_root():
    return {"message": "IKEA Backend is running! SO IT WORKS"}