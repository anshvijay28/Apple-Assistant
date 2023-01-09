from twilio.rest import Client
import openai
from keys import get_keys

def get_description(message):
    l1 = message.split()
    l2 = l1[1:len(l1)]
    return "".join(l2)

openai.api_key = get_keys()['openai_api_key']

def generate_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

account_sid = get_keys()['twilio_account_sid']
auth_token = get_keys()['twilio_auth_token']
client = Client(account_sid, auth_token)

def send_image(receiver, url):
    message = client.messages.create(
                                  from_='+16515656431',
                                  media_url=[url],
                                  to=receiver
                                )