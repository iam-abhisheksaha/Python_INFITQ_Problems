
num1=int(input("Enter the Starting number :- "))
num2=int(input("Enter the Ending number :- "))

number1=0
number2=0
numbers=[]
i=num1
while i<=num2:
    
    if i>9 and i<=99:
        
        number1=i%10
        number2=int(i/10)
        
        if int(number1+number2)%3==0:
            
            if i%5==0:
                
                numbers.append(i)
                
        # print(number1,number2)
    
    
    i=i+1

print(max(numbers))
        
        
        
