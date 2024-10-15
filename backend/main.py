from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
"""
This module defines a FastAPI application for managing a list of medicines.
It provides endpoints to retrieve all medicines, retrieve a single medicine by name,
and create a new medicine.
Endpoints:
- GET /medicines: Retrieve all medicines from the data.json file.
- GET /medicines/{med_name}: Retrieve a single medicine by name from the data.json file.
- POST /medicines/create: Create a new medicine with a specified name and price.
Functions:
- get_all_meds: Reads the data.json file and returns all medicines.
- get_single_med: Reads the data.json file and returns a single medicine by name.
- create_med: Reads the data.json file, adds a new medicine, and writes the updated data back to the file.
Usage:
Run this module directly to start the FastAPI application.
"""
import uvicorn
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/medicines")
def get_all_meds():
    with open('data.json') as meds:
        data = json.load(meds)
    return data

@app.get("/medicines/{med_name}")
def get_single_med(med_name: str):
    with open('data.json') as meds:
        data = json.load(meds)
        for med in data["medicines"]:
            print(med)
            if med['name'] == med_name:
                return med
    return {"error": "Medicine not found"}

@app.post("/medicines/create")
def create_med(name: str = Form(...), price: float = Form(...)):
    with open('data.json', 'r+') as meds:
        current_db = json.load(meds)
        new_med = {"name": name, "price": price}
        current_db["medicines"].append(new_med)
        meds.seek(0)
        json.dump(current_db, meds)
        meds.truncate()
        
    return {"message": f"Medicine created successfully with name: {name}"}

# Add your average function here

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)