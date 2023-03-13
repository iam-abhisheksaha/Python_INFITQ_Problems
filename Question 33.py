def nearest_palindrome(number):
    check=True
    while check:
        temp=number
        rev=0
        while temp>0:
            dig=temp%10
            rev=rev*10+dig
            temp=temp//10
        if(rev==number):
            print(number)
            check=False
        else:
            number=number+1

number=int(input("Enter the Number:- "))

nearest_palindrome(number)