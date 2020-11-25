import sys
import math


n = int(input())
for i in range(n):
    turn = 0
    x = input()
    final_x = x
    
    #While we don't get a happy number and that we haven't tried 100 times to get a happy number
    while (x != "1" and turn < 100):
        x = [int(y)**2 for y in list(x)]
	x = str(sum(x))
    
    #If x equals 1, we have a happy number
    smiley = ":)" if x=="1" else ":("
    print(str(final_x)+" "+smiley)
