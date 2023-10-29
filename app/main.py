from fastapi import FastAPI
from services import developer_service
from services import router as routes_router
import sys
sys.path.insert(0, '.\app\services')


app = FastAPI()

app.include_router(routes_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/function/{desarrollador}")
def get_developer_info(desarrollador: str):
    return developer_service.developer(desarrollador)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
