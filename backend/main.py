from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

@app.get("/medicines")
def read_root():
    with open('data.json') as meds:
        data = json.load(meds)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)