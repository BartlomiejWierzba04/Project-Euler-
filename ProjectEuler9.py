#There exists exactly one Pythagorean triplet for which a+b+c = 1000
#Find the product abc 
import math 


#a^2+b^2=c^2 makes a pythagorean triplet a b c 
#this code is awfullly inefficient btw
def generateTriplets():
    TripletArr = []
    for x in range(1,1000): 
        for y in range(1,1000): 
            result = int(math.sqrt(x**2+y**2))
            if x**2+y**2 == (int(result)**2) and(x+y+result == 1000):
                print(result*x*y)




generateTriplets()
