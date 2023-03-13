
heads=int(input("Enter the Count of the heads :- "))
legs=int(input("Enter the Count of the legs :- "))

if heads>legs:
    print('No Solution')
    
elif (legs%2!=0):
    print("No Solution")
    
else:
    # print("Solution")
    rabbit_headCount= (legs-2*heads)/2
    chicken_headCount= heads-rabbit_headCount
    print(int(rabbit_headCount),int(chicken_headCount))