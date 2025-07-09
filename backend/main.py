from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Appointment(BaseModel):
    name: str
    email: str
    phone: str
    treatment: str
    date: str

@app.post("/appointments")
def save_appointment(appointment: Appointment):
    try:
        data = appointment.dict()
        result = supabase.table("appointments").insert(data).execute()
        print(result)  # DEBUGGING LINE
        return {"message": "Appointment saved successfully"}
    except Exception as e:
        print(f"❌ ERROR: {e}")  # DEBUGGING LINE
        return {"error": "Failed to save appointment"}


