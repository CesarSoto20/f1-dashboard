from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def get_root():
    return {"message": "Hello, World!"}




@app.get("/drivers")
def get_drivers():
    drivers = [
        {"id": 1, "name": "Max Verstappen", "team": "Red Bull Racing"},
        {"id": 2, "name": "Lewis Hamilton", "team": "Ferrari"},
    ]
    return drivers 