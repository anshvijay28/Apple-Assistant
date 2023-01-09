import json 

"""
secrets_filename = 'encryption'
api_keys = {}
with open(secrets_filename, 'r') as f:
	api_keys = json.loads(f.read())

print(api_keys)
"""

f = open('encryption.json')
keys = json.load(f)

print(keys['twilio_auth_token'])

f.close()