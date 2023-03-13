from tkinter import Variable


def primeCheck(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    
    if count==2:
        return 1
    else:
        return 0


number=input("Enter a number:- ")
num_length=len(number)

variable=int(number)
rem=0
sum=0
i=0
while i<num_length:
    rem=int(variable%10)
    variable=int(variable/10)
    variable=(rem*(10**(num_length-1))+variable)
    check=primeCheck(variable)
    sum=sum+check
    
    i=i+1
if sum==num_length:
    print('Circular PrimeNumber')
else:
    print('Not Circular PrimeNumber')