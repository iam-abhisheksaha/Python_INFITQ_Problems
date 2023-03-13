
# Enter the Credit Card Number
creditCardNumber=int(input())
# print(creditCardNumber)
indiCardNumber=[]

# Break the Credit Card Number into individual digits
while creditCardNumber!=0:
    remainder=creditCardNumber%10
    indiCardNumber.append(remainder)
    creditCardNumber=int(creditCardNumber/10)

# Reverse the String
indiCardNumber=indiCardNumber[::-1]

# Multiply and Add based upon the Algo
sum=0
for i in range(len(indiCardNumber)):
    
    if i%2!=0:
        indiCardNumber[i]=indiCardNumber[i]*2

        if indiCardNumber[i]>9:
            while indiCardNumber[i]!=0:
                remainder=indiCardNumber[i]%10
                # print(remainder)
                sum=sum+remainder
                indiCardNumber[i]=int(indiCardNumber[i]/10)
            indiCardNumber[i]=sum
            sum=0

# Sum all the individual digits
sum=0
for i in range(len(indiCardNumber)):
    sum=sum+indiCardNumber[i]

if sum%10==0:
    print("This is a valid card")
else:
    print("This is not a valid card")

