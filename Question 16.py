
airline=input('Enter the name of the Airline:- ')

sourse=input('Enter the Sourse:- ')
sourse=sourse[:3]

destination=input('Enter the destination:- ')
destination=destination[:3]

no_of_passengers =int(input('Enter the number of passengers: '))
start=101

ticket=[]

for i in range(no_of_passengers):  
    
        temp=airline+":"+sourse[0:3]+":"+destination[0:3]+":"+ str(start)
        ticket.append(temp)
        start=start+1

if no_of_passengers<5:
    print(ticket)

else:
    print(ticket[-5:])
    
    