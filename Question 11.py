
year= int(input('Enter the year: '))

leap_count=0
leap_year=[]

while leap_count<=15:
    
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                leap_year.append(year)
                leap_count=leap_count+1
                year=year+1
            else:
                year=year+1      
        else:
            leap_year.append(year)
            leap_count=leap_count+1
            year=year+1
    else:
        year=year+1
        
    
   


print(leap_year)
                
                