from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "IKEA Backend is running! SO IT WORKS"}