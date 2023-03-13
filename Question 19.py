
string1=input("Enter the String:- ")
string1=list(string1)
print(string1)
final_list=[]

check_letter=string1[0]
count=0
print(len(string1))
i=0
while i<=len(string1):
    # print(i)
    
    if check_letter == string1[i]:
        count+=1
        check_letter=string1[i]
    
    else:
        final_list.append(str(count))
        final_list.append(check_letter)
        check_letter=string1[i]
        count=1
    i=i+1


final=''.join(final_list)
print(final_list)
print(final)

    
    
        