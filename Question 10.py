
rupees1_note=int(input())
rupees5_note=int(input())
five_count=-1
one_count=0
amount=int(input())

temp_amount=0

while temp_amount<=amount or rupees5_note==0:
    
    temp_amount=temp_amount+5
    rupees5_note=rupees5_note-1
    five_count=five_count+1

real_amount=temp_amount-5
# print(five_count)
diff=amount-real_amount

if diff<=rupees1_note:
    one_count=diff
    print(five_count)
    print(one_count)
else:
    print(-1)
