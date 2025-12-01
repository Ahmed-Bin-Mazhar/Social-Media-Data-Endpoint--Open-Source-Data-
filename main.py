from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from typing import Optional
import threading
import time

app = FastAPI(title="Disaster Data API")

# Global variable to simulate online/offline
service_online = False

# Load CSV into memory on startup
try:
    df = pd.read_csv("pakistan_disaster_mega_dataset.csv")
except FileNotFoundError:
    df = pd.DataFrame()
    print("CSV file not found. Please check the file path.")

@app.get("/status")
def get_status():
    """
    Returns the online/offline status of the service
    """
    return {"status": "online" if service_online else "offline"}

@app.post("/toggle")
def toggle_service():
    """
    Toggle the service status between online/offline
    """
    global service_online
    service_online = not service_online
    return {"new_status": "online" if service_online else "offline"}

@app.get("/data")
def get_data(id: Optional[str] = None, lang: Optional[str] = None):
    """
    Fetch data from CSV in JSON format.
    Optional filters: id, lang
    """
    if not service_online:
        raise HTTPException(status_code=503, detail="Service is offline")

    filtered_df = df

    if id:
        filtered_df = filtered_df[filtered_df["id"] == id]

    if lang:
        filtered_df = filtered_df[filtered_df["lang"] == lang]

    # Convert dataframe to JSON
    result = filtered_df.to_dict(orient="records")
    return JSONResponse(content=result)
