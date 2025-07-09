# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



### 📄 actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests

class ActionSaveAppointment(Action):
    def name(self) -> Text:
        return "action_save_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phone = tracker.get_slot("phone")
        treatment = tracker.get_slot("treatment")
        date = tracker.get_slot("date")

        # Call FastAPI backend to save data (replace with your endpoint)
        payload = {
            "name": name,
            "email": email,
            "phone": phone,
            "treatment": treatment,
            "date": date
        }
        try:
            response = requests.post("http://localhost:8000/appointments", json=payload)
            if response.status_code == 200:
                dispatcher.utter_message(text=f"Appointment booked for {name} on {date} for {treatment}.")
            else:
                dispatcher.utter_message(text="Something went wrong while booking.")
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to contact backend: {e}")

        return [SlotSet("name", name), SlotSet("treatment", treatment), SlotSet("date", date)]

