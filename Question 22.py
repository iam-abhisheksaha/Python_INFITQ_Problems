def find_pairs_of_numbers(num_list,ideal_num):
    # print(ideal_num)
    # print(num_list)
    i=0
    
    count=0
    while i<len(num_list):
        j=i+1
        while j<len(num_list):
            
            if ideal_num==num_list[i]+num_list[j]:
                count+=1
                num_list.remove(num_list[j])
                
            elif ideal_num==num_list[j]:
                count+=1
                num_list.remove(num_list[j])
            
            j=j+1
        i=i+1
        
    
    print(count)
    print(num_list)


n=int(input("Enter the size of the List:- "))
num_list=[]

for i in range(n):
    temp_num=int(input("Enter the num:- "))
    num_list.append(temp_num)

# print(num_list)
ideal_num=int(input("Enter the number:- "))
find_pairs_of_numbers(num_list,ideal_num)
