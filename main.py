
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory config (simulate DB)
feature_config = {
    "Cyberpunk Style": {"tier": 4, "enabled": True},
    "High Resolution (1536x1536)": {"tier": 16, "enabled": False},
    "Sandbox Chat": {"tier": 8, "enabled": True},
    "Negative Prompt": {"tier": 8, "enabled": True},
    "Experimental Styles": {"tier": 32, "enabled": False},
}

class ToggleRequest(BaseModel):
    feature_name: str

@app.get("/features")
def get_features():
    return feature_config

@app.post("/toggle")
def toggle_feature(req: ToggleRequest):
    if req.feature_name not in feature_config:
        raise HTTPException(status_code=404, detail="Feature not found")
    feature_config[req.feature_name]["enabled"] = not feature_config[req.feature_name]["enabled"]
    return {"status": "success", "new_state": feature_config[req.feature_name]}
