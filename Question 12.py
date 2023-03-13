
#Shop Input

shopGem_count=int(input('How many Gems the Shop wants to display? :- '))

gems_list=[]
prices_list=[]

for i in range(shopGem_count):
    
    gem=input('Gem Name:- ')
    gems_list.append(gem)
    
    price=int(input('Price: :- '))
    prices_list.append(price)

# print(gems_list)
# print(prices_list)

#Buyer Input

buyerGem_count=int(input('How many Gems you want to buy? :- '))

request_gem=[]
gem_count=[]

for i in range(buyerGem_count):
    
    gem=input('Gem Name:- ')
    request_gem.append(gem)
    
    count=int(input('Number of gems:- '))
    gem_count.append(count)

# print(request_gem)
# print(gem_count)
total_price=0
count=0
for i in range(buyerGem_count):
    
    for j in range(shopGem_count):
        
        if request_gem[i]==gems_list[j]:
            
            quantity= gem_count[i]
            price=prices_list[j]
            total_price=total_price+(quantity*price)
        
        else:
            count=count+1
            if count>=buyerGem_count:
                total_price=total_price-1
                count=0

if total_price>30000:
    total_price=total_price-((total_price*5)/100)
print(total_price)
# print(quantity)
# print(price)