adults=int(input('How many adults?'))
kids=int(input('How many children?'))

adult_rate=37550*adults
kids_rate=(37750/3)*kids
fare= adult_rate+kids_rate
total_discount= (fare*3)/100

total_fare=fare-total_discount
print(total_fare)