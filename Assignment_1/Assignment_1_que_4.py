# enter marks and get them in sorted manner

n = 5  # we can even have input from user here
li = [] 

for i in range(n): 
    x = int(input()) 
    li.append(x) 

li.sort() 

print()

for j in li:
    print(j) 