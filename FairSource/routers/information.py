from fastapi import APIRouter
from FairSource.schemas.information_check import BaseResponse
from FairSource.services import sources_service

router = APIRouter()

@router.get("/baseInfo", response_model=list[BaseResponse])
def get_baseInfo():
    return sources_service.get_baseInfo()

@router.get("/regionSources")
def get_region_sources(region: str):
    return sources_service.get_regionInfo(region)