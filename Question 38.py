from re import I
def sum_of_numbers(oddNumbers,evenNumbers):
    
    choice=input('Enter your choice:- ')
    if choice=='Odd':
        sum_odd=0
        for i in oddNumbers:
            sum_odd=sum_odd + i
        
        print(f'Sum of Odd Numbers:- {sum_odd} ')
    
    if choice=='Even':
        sum_even=0
        for i in evenNumbers:
            sum_even=sum_even + i
        
        print(f'Sum of Even Numbers:- {sum_even}')
    
    if choice=='All':
        sum_odd=0
        for i in oddNumbers:
            sum_odd=sum_odd + i
            
        sum_even=0
        for i in evenNumbers:
            sum_even=sum_even + i
        
        total_sums=sum_even+sum_odd
        print(f'Total Sums:- {total_sums}')
    
        

def odd(start, end):
    odd_nums=[]
    i=start
    while i<end:
        if i%2!=0:
            odd_nums.append(i)
        
        i=i+1
    return odd_nums

def even(start, end):
    even_nums=[]
    i=start
    while i<end:
        if i%2==0:
            even_nums.append(i)
        
        i=i+1
    return even_nums


start=int(input("Enter the starting Number:- "))
end=int(input("Enter the ending Number:- "))

oddNumbers=odd(start, end)
evenNumbers=even(start, end)
sum_of_numbers(oddNumbers,evenNumbers)
print(f'Odd Number are {oddNumbers}')
print(f'Even Number are {evenNumbers}')