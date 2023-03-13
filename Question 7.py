number= int(input())

if number%3==0 and number%5!=0:
    print('Zip')

elif number%5==0 and number%3!=0:
    print('Zap')
    
elif number%5==0 and number%3==0:
    print('Zoom')