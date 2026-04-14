# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Add this import!
from pydantic import BaseModel 
from pipeline import AgentPipeline 

app = FastAPI()

# ---------------------------------------------------------
# CORS SECURITY CONFIGURATION
# ---------------------------------------------------------
# This tells the browser: "Yes, it is safe to talk to me!"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In a real app, you'd put "http://localhost:5173" here
    allow_credentials=True,
    allow_methods=["*"], # This allows the secret OPTIONS request to pass through
    allow_headers=["*"],
)

# We start our pipeline manager exactly once when the server boots up.
manager = AgentPipeline()

# ---------------------------------------------------------
# DATA VALIDATION
# ---------------------------------------------------------
class PlanRequest(BaseModel):
    goal: str

# ---------------------------------------------------------
# OUR API ENDPOINTS
# ---------------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to the Sports Planner Agent API!"}

@app.post("/plan")
def create_and_execute_plan(request: PlanRequest):
    print(f"📥 [API] Received new goal from user: {request.goal}")
    final_output = manager.run(request.goal)
    return final_output