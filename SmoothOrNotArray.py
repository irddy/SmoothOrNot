import time

print("Hello user :)")

time.sleep(1) 

n = int(input("Enter the size of the array: ")) 

count = 0
theArray = [] 

time.sleep(1) 

for i in range(0,n): 
  x = int(input("Enter a number: "))

  theArray.append(x)

for i in range(0,n-1): 
  if abs(theArray[i+1]) - abs(theArray[i]) <= 1: 
    count+=1
  else:
    count
    
time.sleep(1) 

if count == n-1: 
  print("YES")
else:
  print("NO")


time.sleep(0.5)
print("Author: Irdi Duka")
time.sleep(0.5)
print("Time of creation: 9th of July 2020, 17:00")
time.sleep(0.5)
print("Thank you for using the program. Hope you are satisfied")
