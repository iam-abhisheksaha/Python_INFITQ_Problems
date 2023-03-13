import math

def primeFactors(n):
    prime_factors=[]
    # print("Prime")
    while n%2==0:
        prime_factors.append(2)
        n=int(n/2)
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            prime_factors.append(i)
            n=int(n/i)
    
    if n>2:
        prime_factors.append(n)
    
    return prime_factors



n=int(input("Enter the Number:- "))
sum=0
new_n=n+8
while n<=new_n:
    temp=primeFactors(n)
    # print(temp)
    max_prime_factor=max(temp)
    # print(max_prime_factor)
    sum=sum+max_prime_factor
    n=n+1

print(sum)
    
