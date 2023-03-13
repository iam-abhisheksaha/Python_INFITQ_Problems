def find_duplicates(list):
    temp_list = []
    duplicates_list = []
    
    for i in list:
        if i not in temp_list:
            temp_list.append(i)
        else:
            duplicates_list.append(i)
    
    print(duplicates_list)
        
    

length=int(input("Enter the length of the List:- "))
list=[]
for i in range(length):
    
    number=int(input("Enter the number:- "))
    list.append(number)

find_duplicates(list)