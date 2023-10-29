from fastapi import APIRouter
from services.developer_service import developer

router = APIRouter()


@router.get("/developer/{desarrollador}")
def get_developer_data(dev_name: str):
    return developer(dev_name)
