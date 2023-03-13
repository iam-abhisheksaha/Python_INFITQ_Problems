def split(word):
    return [char for char in word ]

def check_anagram(string1,string2):
    
    split_string1 = []
    split_string2 = []
    split_string1=split(string1)
    split_string2=split(string2)
    
    # print(split_string1)
    # print(split_string2)
    i=0
    count=0
    couter=0
   
    while i<len(split_string1):
        j=0
        while j<len(split_string2):
            
            if split_string1[i]==split_string2[j]:
                couter+=1
                break
            j=j+1
        i=i+1
    
    # print(couter)
    i=0
    while i<len(split_string1):
        # print(split_string1[i])
        if split_string1[i]!=split_string2[i]:
            count+=1
        i=i+1
    # print(count)
    if count==len(split_string1) and couter==len(split_string1) and len(split_string1)==len(split_string2):
        print(True)
    else:
        print(False)


string1=input("Enter the first string:- ")
string2=input("Enter the second string:- ")

check_anagram(string1, string2)