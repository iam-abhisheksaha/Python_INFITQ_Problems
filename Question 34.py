#break a word in alphabet
from operator import le
from re import L


def split(word):
    return [char for char in word]

def encrypt_sentence(list):
    # print(list)
    new_list=[]
    temp_list=[]
    counter=0
    i=0
    word_list=[]
    for i in list:
        # print(i)
        if counter == 0 or counter%2==0:
            i=i[::-1]
            new_list.append(i)
        
        else:
            vowel=['a','e','o','u','i']
            result=[letter for letter in i if letter.lower() not in vowel]
            # print(result)
            vowel_result=[letter for letter in i if letter.lower() in vowel]
            # print(vowel_result)
            final_list= result+vowel_result
            final_list=''.join(final_list)
            new_list.append(final_list)
            # print(final_list)
            
            
        counter=counter+1
    new_list=' '.join(new_list)
    print(new_list)

        

string=input("Enter:- ")
list=[]
list.append(string)

# Break a string into words
list=list[0].split()
encrypt_sentence(list)




