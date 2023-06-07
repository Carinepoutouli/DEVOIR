from pydantic import BaseModel

class Vehicle(BaseModel):
    license_plate: str
    owner: str
    category: str
    insurance_quote: float
    markup: float
    total_bill: float

class Bill(BaseModel):pip -m venv env
    owner: str
    license_plates: List[str]
    total_bill: float
