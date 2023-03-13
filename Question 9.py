print('Enter 3 Number')

number=[]
for i in range(3):
    # print(i)
    temp_num=int(input())
    number.append(temp_num)

# print(number)
final_value=1
final_value2=1
contains_seven= 7 in number
# print(contains_seven)

if contains_seven==False:
    for i in range(len(number)):
        final_value2=final_value2*number[i]


else:
    for i in range(len(number)):
    
        if number[i]==7:
            j=i+1
            while j<=len(number)-1:
                # print(number[j])
                final_value=final_value*number[j]
                j+=1
            
        elif number[len(number)-1]==7:
            final_value=-1

    
# print(final_value)
# print(final_value2)
if contains_seven==True:
    print(final_value)
elif contains_seven==False:
    print(final_value2)
    
    