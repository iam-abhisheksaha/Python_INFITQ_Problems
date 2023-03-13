def split(word):
    return [char for char in word]

def find_correct(d):
    CORRECT=0
    ALMOST_CORRECT=0
    WRONG=0
    key_list=[]
    value_list=[]
    for key,value in d.items():
        
        key_list=split(key)
        value_list=split(value)
        check_counter=0
        if key==value:
            CORRECT=CORRECT+1
        
        else:
            i=0
            while i<len(key_list):
                # print(i)
                j=i
                if key_list[i]!=value_list[j]:
                    check_counter+=1
                
                i=i+1
            
            # print(check_counter)
            
            if check_counter<=2:
                ALMOST_CORRECT=ALMOST_CORRECT+1
            
            elif check_counter>2:
                WRONG=WRONG+1
        
        
    print(CORRECT)
    print(ALMOST_CORRECT)
    print(WRONG)
        


num=int(input("Enter how many words needed to be checked:- "))
n=num
d = dict(input("Enter key and value: ").split() for _ in range(n))

# print(d)

find_correct(d)