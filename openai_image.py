from twilio.rest import Client
import openai

def get_description(message):
    l1 = message.split()
    l2 = l1[1:len(l1)]
    return "".join(l2)

openai.api_key = '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'

def generate_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

account_sid = 'AC305c3aed3f154982ae4d14a80c088ea4'
auth_token = '1d905e3916217418b8573c1614658621'
client = Client(account_sid, auth_token)

def send_image(receiver, url):
    message = client.messages.create(
                                  from_='+16515656431',
                                  media_url=[url],
                                  to=receiver
                                )










