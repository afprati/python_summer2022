# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest (best rating and closest)?
# 3) if I wanted to hold an upscale evening meeting there, which fancy bar would you suggest? 
# for 2 and 3, you will need to enable the google places API
# you may find this page useful to learn about different findinging nearby places https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/


import importlib 
import os
import googlemaps

os.chdir('C:\\Users\\Tita\\Documents\\GitHub\\python_summer2022\\Day6\\Lab')
imported_items = importlib.import_module('start_google')
gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
# Locate the white house
wh_location = gmaps.geocode(whitehouse)
wh_location # location is a list of dictionaries

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]
embassies[0]

# Get keys
wh_location[0].keys()
# Get geometry
wh_location[0]['geometry'].keys()
# Get location
wh_location[0]['geometry']['location']


# Store latlong
latlong = wh_location[0]['geometry']['location']


# Get the destination using latlong
destination = gmaps.reverse_geocode(latlong)

locations = ""



