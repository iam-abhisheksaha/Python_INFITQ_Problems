
def find_ten_substring(num_str):
    
    i=0   
    find_substring=[]
    while i<=len(num_str):
        find_substring.append(num_str[i])
        sum=num_str[i]
        j=0
        while j<=len(num_str):
            find_substring.append(num_str[j])
            if num_str[j]==num_str[i]:
                j=j+1
            
            sum=sum+num_str[j]
            
            if sum==10:
                for k in find_substring:
                    
                
            
            




num= int(input("Enter the Number:- "))
num_str=[]

while num!=0:
    
    temp=int(num%10)
    num_str.append(temp)
    num=int(num/10)
    

# print(num_str)
find_ten_substring(num_str)