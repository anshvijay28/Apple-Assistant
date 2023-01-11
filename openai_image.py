from twilio.rest import Client
import openai
import os
import variables

def get_description(message):
    l1 = message.split()
    l2 = l1[1:len(l1)]
    return "".join(l2)

openai.api_key = os.environ['openaiApiKey']

def generate_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

account_sid = os.environ['twilioAccountSid']
auth_token = os.environ['twilioAuthToken']
client = Client(account_sid, auth_token)

def send_image(receiver, url):
    message = client.messages.create(
                                  from_= os.environ['numberFrom'],
                                  media_url=[url],
                                  to=receiver
                                )


    