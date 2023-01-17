import temperature

def get_subject():
	subject = str(temperature.CITY) + ": " + "It's " + str(temperature.current_date) + "!"
	return subject
def get_body():
	body = '''
	It currently feels like {feels_like} degrees.
	The actual temperature is {actual} degrees.
	The low today will be {low} degrees.
	The high today will be {high} degrees.
	The sun will set at {sunset}.
	'''.format(feels_like = str(temperature.feels_like), actual = str(temperature.actual),
		low = str(temperature.low), high = str(temperature.high), 
		sunset = str(temperature.time_of_sunset))
	return body 