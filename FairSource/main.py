from fastapi import FastAPI
from FairSource.routers import connection
from FairSource.routers import information
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(connection.router)
app.include_router(information.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "IKEA Backend is running! SO IT WORKS"}