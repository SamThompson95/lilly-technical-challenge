from fastapi import FastAPI, Form
import uvicorn
import json

app = FastAPI()

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
def create_med(id: int = Form(...), name: str = Form(...), price: float = Form(...)):
    with open('data.json', 'r+') as meds:
        current_db = json.load(meds)
        new_med = {"id": id, "name": name, "price": price}
        current_db["medicines"].append(new_med)
        meds.seek(0)
        json.dump(current_db, meds)
        meds.truncate()
        
    return {"message": "Medicine created"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)