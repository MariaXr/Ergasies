"""
Name          :
Surname       :
Programm Title: Tetris game for array 10x20 to count how many L can be added in random position.
Date          :
Description   : The game exists when the L can't be added in the random position and is printing the counter.
"""
import random
import sys
#initialize the counter of L
countL=0;
#function to check where to add the L in the array in a specific position
def checkPutLinArray(dataArray,position):
	rows=20;
	columns=10;
	len_array = 20;
	foundRow = -1;
	for row in range(rows):
		#check if it is allow to add the L in the row 
		if(dataArray[row][position]!="|" and dataArray[row][position+1]!="|"):
			foundRow = row;
		#else the possible row is the previous that you found
		else:
			break;
	#if the row is less or equal than 1 that means L is not allow to be added. Print the counter of L and exit the program.
	if(foundRow<=1):
		print(countL);
		sys.exit();
	putLinArray(dataArray,foundRow,position);	
#function to add the L in the array in a specific position
def putLinArray(dataArray,foundRow,column):
	dataArray[foundRow][position]="|";
	dataArray[foundRow-1][position]="|";
	dataArray[foundRow-2][position]="|";
	dataArray[foundRow][position]="|";
	dataArray[foundRow][position+1]="|";
	return dataArray;
dataArray = [[" "]*10 for _ in range(20)]
while(True):
	#get random position from 0 to 9
	position=random.randrange(0,9);
	checkPutLinArray(dataArray,position);
	countL+=1;