a = list(input().split())
b = 0

for i in a:
    if i == 'name':
        b = b + 1 

if b > 0:
    print("YES")
else:
    print("NO") 