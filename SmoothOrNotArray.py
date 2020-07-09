import time

print("Hello user :)")

time.sleep(1) 

n = int(input("Enter the size of the array: ")) 

count = 0
theArray = [] 

for i in range(0,n): 
  x = int(input("Enter a number: "))

  theArray.append(x)

for i in range(0,n-1): 
  if abs(theArray[i+1]) - abs(theArray[i]) <= 1: 
    count+=1
  else:
    count

if count == n-1: 
  print("YES")
else:
  print("NO")