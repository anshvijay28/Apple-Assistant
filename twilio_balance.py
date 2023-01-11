from twilio.rest import Client
import variables
import os

account_sid = os.environ['twilioAccountSid'] 
auth_token = os.environ['twilioAuthToken']

client = Client(account_sid, auth_token)

def get_balance():

	balance_data = client.api.v2010.balance.fetch()
	balance = float(balance_data.balance)
	currency = balance_data.currency

	message = f'Your account has {balance:}{currency} left.'
	return message
