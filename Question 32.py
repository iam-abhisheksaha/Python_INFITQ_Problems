number=int(input("Enter the Number:- "))
temp_number=number
temp_number2=number
count=0
while temp_number!=0:

    count=count+1
    temp_number=int(temp_number/10)

new_number=0

while temp_number2!=0:
    
    temp=temp_number2%10
    # print(temp**count)
    new_number=new_number+(temp**count)
    temp_number2=int(temp_number2/10)

# print(new_number)
if new_number==number:
    print("It's an Armstrong Number")
else:
    print("It's not an Armstrong Number")
    
    