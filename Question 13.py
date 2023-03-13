
print('Enter the lenght of the three sides of triangle :- ')

x=input('Enter 1st Lenght :- ')
y=input('Enter 2nd Lenght :- ')
z=input('Enter 3rd Lenght :- ')

if x<y+z and y<z+x and z<x+y:
    print('Triangle can be formed')
else:
    print('Triangle cannot be formed')
