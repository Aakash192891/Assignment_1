# lists 

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
for i in range(len(colour)):
    if colour[i] in ['Black', 'Pink']:
        colour[i] = 'Purple' 

print(colour) 