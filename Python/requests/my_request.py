import os
import sys
import requests

# script that make a request

REQUEST = sys.argv[1]
option_port_param = sys.argv[2] # param port (--port)
PORT = sys.argv[3] # PORT (3000)
option_endpoint_param = sys.argv[4] # param endpoint (--endpoint)
ENDPOINT = sys.argv[5] # endpoint url path
try:
	str(option_port_param)
	int(PORT)
	str(option_endpoint_param)
	str(ENDPOINT)
except:
	raise ValueError("Not correct, please try again")

def my_request(request, pport, PORT, pend, ENDPOINT):
	"""
	This is my personal script that make a simple GET or POST request only for localhost
	params:
		-request GET or POST
		-pport is the option passed in a script '--port'
		-PORT is the port 
		-pend is the endpoint url that you append in localhost
		-ENDPOINT is the path of your local web server
	"""
	# print request, pport, pend, PORT, ENDPOINT
	try:
		if request != 'GET' and request != 'POST':
			raise KeyError("Pass an HTTP verb method correctly, please try again")
		if pport != '--port' or pend != '--endpoint':
			raise KeyError("Pass the correct param --port or --endpoint")
	except KeyError as k:
		raise k
	if request == 'GET':
		r = requests.get('http://localhost:{}{}'.format(PORT, ENDPOINT))
	elif request == 'POST':
		r = requests.post('http://localhost:{}{}'.format(PORT, ENDPOINT), data = {'first_name':'Maurizio', 'last_name': 'Bussi', 'email': 'mauriziocontatto@gmail.com', 'username': 'mauridb', 'password': 'ciccia puzza e molla'})

	else:
		print 'NOT ALLOWED METHOD!'

my_request(REQUEST, option_port_param, PORT, option_endpoint_param, ENDPOINT)

