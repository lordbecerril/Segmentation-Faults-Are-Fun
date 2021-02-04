# Practice for an upcoming interview
# HTTP means Hypertext Transfer Protocol
# HTTP is used for communication between clients and servers
# GET: requests data from the server
# POST: Submits data to be processed by the server
# three libraries which are used for HTTP in python are httplib, urllib, and requests
# Let us learn requests


# Importing Requests Library
import requests

# Get the API endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"


location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

print(data)
