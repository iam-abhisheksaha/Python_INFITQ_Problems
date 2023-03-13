from collections import OrderedDict

def remove_duplicate(str):
    return "".join(OrderedDict.fromkeys(str))

str=input("Enter a String:- ")

print(remove_duplicate(str))
