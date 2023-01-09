from twilio.rest import Client
from keys import get_keys

account_sid = get_keys()['twilio_account_sid']
auth_token = get_keys()['twilio_auth_token']

client = Client(account_sid, auth_token)

def get_balance():

	balance_data = client.api.v2010.balance.fetch()
	balance = float(balance_data.balance)
	currency = balance_data.currency

	message = f'Your account has {balance:}{currency} left.'
	return message
print(get_balance())