import temperature

def get_subject():
	subject = str(temperature.CITY) + ": " + "It's " + str(temperature.current_date) + "!"
	return subject
def get_body():
	body = '''

	It currently feels {feels_like}°F.
	The real temperature is {actual}°F.
	The low today will be {low}°F.
	The high today will be {high}°F.
	The sun will set at {sunset}.
	'''.format(feels_like = str(temperature.feels_like), actual = str(temperature.actual),
		low = str(temperature.low), high = str(temperature.high), 
		sunset = str(temperature.time_of_sunset))
	return body

