"""
Name          :
Surname       :
Programm Title: Rotate Array 8x8in clockwise
Date          :
Description   : Read from file an array 8x8 with spaces and 0 and show the 3 rotation of that array.
"""
#function for printing 2D array
def printArray(dataArray):
	rows=8;
	columns=8;
	for row in range(rows):
		columnValue = "";
		for column in range(columns):
			if(column==7):
				columnValue +=str(dataArray[row][column]);
			else:
				columnValue +=str(dataArray[row][column]) + ",";
		print(columnValue);
#function to rotate clockwise array
def rotateArray(dataArray):
	dataArrayRotate = [[""]*8 for _ in range(8)]
	rows=8;
	columns=8;
	len_array = 8;
	for rotateRow in range(rows):
		for row in range(rows):
			dataArrayRotate[rotateRow][row]=dataArray[len_array-1-row][rotateRow].rstrip('\r\n');
	return dataArrayRotate;
#Read the file
fin=open("array8x8.txt","r");
#dataArray = [str("test")]*8*8;

dataArray = [[""]*8 for _ in range(8)]
#dataArray=[][];
rows=0;
columns=0;
#read lines
lines = fin.readlines();
#for each line add the values in array
for line in lines:
	data = line.split(",");
	dataValue = "";
	for d in data:
		dataValue += str(d);
		dataArray[rows][columns] = str(d);
		columns += 1;
	rows += 1;
	columns = 0;
dataArrayRotate1 = rotateArray(dataArray);
dataArrayRotate2 = rotateArray(dataArrayRotate1);
dataArrayRotate3 = rotateArray(dataArrayRotate2);
print("Rotate 1");
printArray(dataArrayRotate1);
print("Rotate 2");
printArray(dataArrayRotate2);
print("Rotate 3");
printArray(dataArrayRotate3);