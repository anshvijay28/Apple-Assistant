import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("openai_api_key", None)
openweathermap_api_key=os.getenv("openweathermap_api_key", None)
twilio_account_sid=os.getenv("twilio_account_sid", None)
twilio_auth_token=os.getenv("twilio_auth_token", None)
number_to=os.getenv("number_to", None)
number_from=os.getenv("number_from", None)

