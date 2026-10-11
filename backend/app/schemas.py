from pydantic import BaseModel



class DriverResponse(BaseModel):
    id: int
    name: str
    team: str
   