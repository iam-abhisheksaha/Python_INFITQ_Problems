def check_double(number):
    split_number = [int(a) for a in str(number)]
    double_num=2*number
    split_double_number = [int(a) for a in str(double_num)]
    count=0
    i=0
    while i<len(split_number):
        j=0
        # print(split_number[i])
        while j<len(split_double_number):
            
            if split_number[i] == split_double_number[j] and i!=j:
                count+=1
                # print(split_number[j])
            j=j+1
        i=i+1
    
    # print(count)
    if count==len(split_double_number):
        return True
    else:
        return False


number=int(input('Enter the Number:- '))

yoo=check_double(number)
print(yoo)
