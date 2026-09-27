from fastapi import APIRouter

router = APIRouter()


@router.get("/connection")
def check_connection():
    return {
        "status": "connected",
        "message": "👍"
    }