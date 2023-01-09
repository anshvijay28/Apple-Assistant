import json

def get_keys():
	f = open('encryption.json')
	keys = json.load(f)
	f.close()
	return keys