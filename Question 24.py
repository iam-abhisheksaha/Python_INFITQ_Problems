def create_largest_number(num_list):
    num_list.sort(reverse=True)
    s = [str(i) for i in num_list]
    new_list = ("".join(s))
    print(new_list)

n=int(input("Enter the size of List:- "))
num_list=[]

for i in range(n):
    temp_num=int(input("Enter a 2-digit Num:- "))
    num_list.append(temp_num)

# print(num_list)

create_largest_number(num_list)