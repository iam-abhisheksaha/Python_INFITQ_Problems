number=int(input('Enter 3-digit number:- '))
sum=0
temp_number=number
while temp_number>0:
    temp_num=temp_number%10
    sum=sum+temp_num**3
    
    temp_number //= 10

if sum==number:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')
    
    
    

