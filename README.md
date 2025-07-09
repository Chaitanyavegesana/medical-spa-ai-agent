# Medical Spa AI Agent 💆‍♀️🤖

This project is an AI-powered assistant designed for medical spas. It handles appointment bookings, customer follow-ups, treatment recommendations, and promotional interactions—all via a smart AI agent.

## 🌟 Features

- ✅ Book appointments via natural language chat
- 🧠 Intelligent reminders for upcoming/due treatments
- 💡 Recommends new or related skincare treatments
- 💬 Promotes spa products, discounts, and offers
- 📹 Encourages customers to upload experience videos
- 📊 Admin dashboard to manage content, treatments, and promotions
- 🔒 Secure backend with FastAPI and SQLite

## 🛠️ Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| AI Interface  | Rasa (NLU + Core)  |
| Backend API   | FastAPI            |
| Database      | SQLite (via SQLAlchemy) |
| Deployment    | Uvicorn (for API), Rasa server |
| Dashboard     | (Planned) Streamlit or React.js |

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Chaitanyavegesana/medical-spa-ai-agent.git
cd medical-spa-ai-agent

#2. Set up virtual environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# 3. Start services
Run Rasa:
bash
Copy
Edit
rasa train
rasa run actions &
rasa shell
Run Backend API:
bash
Copy
Edit
cd backend
uvicorn main:app --reload --port 8000
#4. Interact with bot
bash
Copy
Edit
rasa shell
📂 Project Structure
bash
Copy
Edit
medical-spa-ai-agent/
├── actions/              # Custom Rasa actions (Python)
├── backend/              # FastAPI app to store appointments
├── data/                 # Training data (nlu, stories)
├── models/               # Trained Rasa models
├── domain.yml            # Intents, entities, responses
├── config.yml            # Rasa pipeline & policies
├── endpoints.yml         # Action server URL
├── README.md
├── LICENSE
🔐 Security
No user data leaves the local environment

FastAPI can be secured with authentication (planned)

👥 Contributing
Pull requests are welcome! For major changes, open an issue first.