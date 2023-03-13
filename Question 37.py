from unittest import result


def split(word):
    return [char for char in word]

def sms_encoding(list_sentence):
    final_list=[]
    for i in list_sentence:
        vowel=['a','e','o','u','i']
        vowel_result=[letter for letter in i if letter.lower() in vowel]
        if len(i) == len(vowel_result):
            final_list.append(i)
        else:
            # remove vowel from a list
            result=[letter for letter in i if letter.lower() not in vowel]
            result=''.join(result)
            final_list.append(result)
    #merge a list into string
    final_list=" ".join(final_list)
    print(final_list)            
        
        
    


sentence=input('Enter the sentence:- ')
list_sentence=[]
list_sentence.append(sentence)

list_sentence=list_sentence[0].split()
# print(list_sentence)
sms_encoding(list_sentence)