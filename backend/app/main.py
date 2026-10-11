from fastapi import FastAPI
from app.schemas import DriverResponse


app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello, World!"}

drivers = [
        {"id": 1, "name": "Max Verstappen", "team": "Red Bull Racing"},
        {"id": 2, "name": "Lewis Hamilton", "team": "Ferrari"},
    ]

@app.get("/drivers",response_model=list[DriverResponse])
def get_all_drivers():
    return drivers 



@app.get("/drivers/{driver_id}", response_model=DriverResponse)
def get_driver(driver_id: int):
    return None