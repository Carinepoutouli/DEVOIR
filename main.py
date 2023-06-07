from fastapi import FastAPI, HTTPException
from typing import List
from models import Vehicle, Bill

app = FastAPI()

# Simulated data for demonstration
vehicles = [
    Vehicle(license_plate="ABC123", owner="Sister Mary", category="car", insurance_quote=1000.0, markup=200.0, total_bill=1200.0),
    Vehicle(license_plate="XYZ789", owner="Sister Anne", category="motorcycle", insurance_quote=800.0, markup=150.0, total_bill=950.0),
    Vehicle(license_plate="DEF456", owner="Sister Margaret", category="car", insurance_quote=1200.0, markup=250.0, total_bill=1450.0)
]

# Endpoint to retrieve vehicles by category
@app.get("/category/{category}")
async def get_vehicles_by_category(category: str):
    filtered_vehicles = [v for v in vehicles if v.category == category]
    return filtered_vehicles

# Endpoint to retrieve vehicles by owner
@app.get("/owner/{owner}")
async def get_vehicles_by_owner(owner: str):
    filtered_vehicles = [v for v in vehicles if v.owner == owner]
    return filtered_vehicles

# Endpoint to generate bill for an owner
@app.get("/bills/{owner}")
async def generate_bill_for_owner(owner: str):
    owner_vehicles = [v for v in vehicles if v.owner == owner]
    if not owner_vehicles:
        raise HTTPException(status_code=404, detail="Owner not found")

    license_plates = [v.license_plate for v in owner_vehicles]
    total_bill = sum(v.total_bill for v in owner_vehicles)
    bill = Bill(owner=owner, license_plates=license_plates, total_bill=total_bill)
    return bill
