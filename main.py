from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import json
import math
from typing import Optional

app = FastAPI(title="Disaster Data API")

# Service status
service_online = True

# Load CSV into memory
df = pd.read_csv("pakistan_disaster_mega_dataset.csv")

def sanitize_value(val):
    """
    Converts NaN or Inf values to None for JSON compatibility.
    """
    if val is None:
        return None
    if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
        return None
    return val

def row_generator_array(filtered_df):
    """
    Generator that yields rows one by one in a JSON array format.
    """
    yield "["  # start of JSON array
    first = True
    for row in filtered_df.to_dict(orient="records"):
        sanitized_row = {k: sanitize_value(v) for k, v in row.items()}
        if not first:
            yield ","
        yield json.dumps(sanitized_row)
        first = False
    yield "]"  # end of JSON array

@app.get("/status")
def get_status():
    """
    Returns online/offline status of the service.
    """
    return {"status": "online" if service_online else "offline"}

@app.post("/toggle")
def toggle_service():
    """
    Toggles the service status between online and offline.
    """
    global service_online
    service_online = not service_online
    return {"new_status": "online" if service_online else "offline"}

@app.get("/data")
def get_data(id: Optional[str] = None, lang: Optional[str] = None):
    """
    Streams CSV data as JSON array. Supports optional filtering by id or lang.
    """
    if not service_online:
        raise HTTPException(status_code=503, detail="Service is offline")

    filtered_df = df.copy()
    if id:
        filtered_df = filtered_df[filtered_df["id"] == id]
    if lang:
        filtered_df = filtered_df[filtered_df["lang"] == lang]

    return StreamingResponse(
        row_generator_array(filtered_df),
        media_type="application/json"
    )
