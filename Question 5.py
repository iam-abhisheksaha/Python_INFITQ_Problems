

total_students =int(input())
# print(total_students)

student_scores=[]

for i in range(total_students):
    # print(i)
    score= int(input())
    student_scores.append(score)
    
total_fees=50000

# print(student_scores)
for i in range(len(student_scores)):
    # print(i)
    percentage=student_scores[i]
    if percentage>=90:
        scholarship=50
        branch='Arts'
        
    elif percentage>85:
        scholarship=50
        branch='Engineering'
        
    elif percentage%7==0:
        scholarship=5
        branch='Engineering'
        
    elif percentage%2!=0 :
        scholarship=5
        branch='Arts'
    
    else:
        scholarship=0
        branch='Gaand Maarao'
        
    
    # print(scholarship)
    # print(branch)
    scholarship_fees=(total_fees*scholarship)/100
    if scholarship>0:
        new_fees=total_fees-scholarship_fees
    else:
        new_fees=total_fees
    
    # print(new_fees)
    print('Student %d' %(i+1))
    print(branch)
    print(new_fees)
    
    
    
    
    