import mimetypes
import os
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from construct_message import get_body
from twilio_balance import get_balance
from openai_image import get_description, generate_image, send_image
from chat_gpt import get_quote

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello, World!"


@application.route("/sms", methods=['GET', 'POST'])
def send_sms():

    body = request.values.get('Body', None)
    body = str(body).lower().strip()

    # Start our TwiML response
    resp = MessagingResponse()
    
    # Logic of which message to respond with 
    if (body == 'hi'):
      resp.message("Hey there!")
    elif (body[0:5] == "gbt: "):
      resp.message(get_gpt_response(body[5:]))
    elif (body == "weather"):
      resp.message(get_body())
    elif (body[:9] == "picture: "):
      description = get_description(body)
      image_url = generate_image(description)
      send_image(os.environ['numberTo'], image_url)
    elif (body == "balance"):
      resp.message(get_balance())
    else:
      resp.message("Please type a valid command.")

    return Response(str(resp), mimetype="application/xml")


if __name__ == "__main__":
  application.run(port=8000)

