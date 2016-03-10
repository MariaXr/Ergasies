"""
Name          :
Surname       :
Programm Title: Opap KINO statistics by input date in format dd-MM-yyyy.
Date          :
Description   : First install the requests module. Open cmd and run for python 3.5 "pip install requests" and 
for python 2.7 "python -m pip install requests".
"""
import requests
print("Input the date you want for KINO statistics in format dd-MM-yyyy");
#Read the input date
date=str(input());
#OPAP KINO web service
url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/";
url+= date + ".json";
response = requests.get(url);
#Get response from KINO web service
data = response.json();
#Split the response with results
data = str(data).split("results");
#Initialize the array of length 80 with 0
statistics = [int(0)]*80;
count=0;
for result in data:
	if(count == 0):
		count += 1;
		continue;
	#Get the draw number
	drawNumbers = result.split("[")[1].split("]")[0];
	#Split with , to get number
	numbers = drawNumbers.split(",");
	#Add the number in the array and add 1 for each number
	for number in numbers:
		position = int(number)-1;
		value = int(statistics[int(position)]);
		value += 1;
		statistics[position]=value;
	count += 1;
print(count);
count=1;
for statistic in statistics:
	print(str(count) + ":" + str(statistic));
	count += 1;
