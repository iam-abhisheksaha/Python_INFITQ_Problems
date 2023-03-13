def find_more_than_average(list_of_marks):
    
    total_marks = sum(list_of_marks)
    average_marks = int(total_marks/10)
    
    count = 0
    for i in range(len(list_of_marks)):
        if average_marks<list_of_marks[i]:
            count += 1
    
    print("The Percentage of Students:- ")
    print(count*10)

def sort_marks(list_of_marks):
    list_of_marks.sort()
    print(list_of_marks)

list_of_marks = []

for i in range(10):
    temp_marks=int(input("Enter the Marks:- "))
    list_of_marks.append(temp_marks)

find_more_than_average(list_of_marks)
sort_marks(list_of_marks)