from twilio.rest import Client

account_sid = 'AC305c3aed3f154982ae4d14a80c088ea4'
auth_token = '1d905e3916217418b8573c1614658621'

client = Client(account_sid, auth_token)

def get_balance():

	balance_data = client.api.v2010.balance.fetch()
	balance = float(balance_data.balance)
	currency = balance_data.currency

	message = f'Your account has {balance:}{currency} left.'
	return message
#print(message)