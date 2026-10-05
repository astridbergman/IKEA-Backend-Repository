from pydantic import BaseModel

class BaseResponse(BaseModel):
    region: str
    score: float