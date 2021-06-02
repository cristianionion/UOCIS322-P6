# UOCIS322 - Project 6 #
Brevet time calculator.

author= Cristian Daniel Ion
email= ion.cristian123@gmail.com
repo= https://github.com/cristianionion/UOCIS322-P5


added RESTful service with json and csv representations to brevet calculator

"http://host:port/listAll" will return open and close times from db
"http://host:port/listCloseOnly" will return just close times
"http://host:port/listOpenOnly" will return just open times

additionally, adding "/json" or "/csv" will specify the output into either json or csv format

if "?top="<int> is added after formatting specification, then only the top <int> times will be returned
	
brevet calculator can be found on the port specified by web in docker-compose.yml
listAll, listCloseOnly, and listOpenOnly can be found on the port specified by restapi in docker-compose.yml

to run: docker-compose up --build in the brevets directory



mongodb and two buttons implemented to brevet calculator

submit button revieves input and inters it into a database
submit also drops previeous database data before inserting the new input

display button takes the data from database and sends it to a new html file. This file shows the user input in a different format.



acp_times.py computes the open and close times of brevet control locations
open and close times depend on the distance of the control locations
to find the times we need, we divide the distance by the rate(distance/time) which will give us the correct time
if a control distance is longer than other control rate ranges, the time is compensated by adding the time from previous rates up until the range of the control distance.
Special case for closing times:
	if the control distance is within 60km of the start, the close time will have an additional hour

	
open times (range, rate):
	 0-200km , 34km/h
	 200-400km , 32km/h
	 400-600km , 30km/h
	 600-1000km , 28km/h
	 1000-1300km , 26km/h
close times (range, rate):
	 0-600km , 15km/h
	 600-1000km , 11.428km/h
	 1000-1300km , 13.333km/h
	 
	 
Ex. opentime: if distance is 350, first 200km have a rate of 34, the last 150km have a rate of 32 so,
	200/34 + 150/32 = decimal value of number of hours = 10.56985
Ex. closetime: if distance is 50, time = 50/15 + 1 = 4.33333...
