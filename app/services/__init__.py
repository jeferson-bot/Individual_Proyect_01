from fastapi import APIRouter
from services.developer_service import developer

router = APIRouter()


@router.get("/developer/{desarrollador}")
def get_developer_data(dev_name: str):
    print("*******************************************************", dev_name)
    return developer(dev_name)


# @app.get("/function")
# def get_developer_info():
#     return developer_service.developer("Kotoshiro")
