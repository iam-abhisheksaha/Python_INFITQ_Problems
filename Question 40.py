

# strig=input("Enter the String:- ")
# lst=list(strig.split(" "))
# print(lst)

sentence=input("Enter the sentence: ")
list_sen=list(sentence.split(" "))
# print(list_sen)

dict_of_counts={item:list_sen.count(item) for item in list_sen}
# print(dict_of_counts)
max_key = max(dict_of_counts, key=dict_of_counts.get)
print(max_key,dict_of_counts[max_key])
