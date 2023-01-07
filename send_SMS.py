import os
from twilio.rest import Client

def send_text_message(receiver, message):
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']

    account_sid = 'AC305c3aed3f154982ae4d14a80c088ea4'
    auth_token = '1d905e3916217418b8573c1614658621'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  body=message,
                                  from_='+16515656431',
                                  # media_url = ['pic link'], USE FLICKR TO GET IMAGES
                                  to=receiver
                              )

    print(message.sid)
    print("Message sent!")

def main():
    send_text_message('+19496367416', 'Reminder!')

if __name__ == "__main__":
    main()
