def is_palindrome(num,temp):
    
    if num == 0:
        return temp
    
    temp=int(temp*10)+int(num%10)
    return is_palindrome(int(num/10),temp)

num=int(input("Enter the Number:- "))
temp_num=num
temp=is_palindrome(num,0)

if temp==temp_num:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")
    

