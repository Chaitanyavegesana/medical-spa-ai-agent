from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Example: Insert a new user
def create_user(name, email, phone):
    response = supabase.table("users").insert({
        "name": name,
        "email": email,
        "phone": phone
    }).execute()
    return response

# Example: Fetch all users
def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data

# Test
if __name__ == "__main__":
    print(get_users())
