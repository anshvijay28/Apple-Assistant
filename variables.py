import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("openai_api_key")
openweathermap_api_key=os.getenv("openweathermap_api_key")
twilio_account_sid=os.getenv("twilio_account_sid")
twilio_auth_token=os.getenv("twilio_auth_token")
number_to=os.getenv("number_to")
number_from=os.getenv("number_from")

