def is_triangle(a, b, c):
    if a > (b+c) or b > (a+c) or c > (a+b):
        print("NO")

    else:
        print("YES")

a = int(input("First side of triangle: "))
b = int(input("Second side of triangle: "))
c = int(input("Third side of triangle: ")) 
is_triangle(a, b, c) 