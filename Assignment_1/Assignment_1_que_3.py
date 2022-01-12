# python program to store different data type values into a list.

li = [] 
Sid = int(input("Enter the Sid: ")) 
name = input("Enter the name of the person: ") 
gender = input("""Specify the gender, 
Use gender values as: 
'M' for male
'F' for female and 
'U' for unknown: """)
course_name = input("Specify the course name: ") 
cgpa = float(input("Enter the cgpa: ")) 

li.append(Sid)
li.append(name) 
li.append(gender) 
li.append(course_name) 
li.append(cgpa)

print(li) 