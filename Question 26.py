def check_quantity_available(item_order,items_quantity,vendor_items,vendor_items_quantity,count):
    # print(vendor_items_quantity)
    if count == 0:
        if item_order in vendor_items:
            return True
        else:
            return False
    if count==1:
        order_index=vendor_items.index(item_order)
        # print(order_index)
        if items_quantity<=vendor_items_quantity[order_index]:
            return True
        else:
            return False
    
def check_quantity(index,items_quantity,vendor_items_quantity):
    vendor_items_quantity[index]=vendor_items_quantity[index]-items_quantity
    print(vendor_items_quantity[index])
       

def place_order(vendor_items,vendor_items_quantity):
    order_number=int(input("Order Number:- "))
    
    
    for i in range(order_number):
        item_order=input("Enter the order:- ")
        item_quantity=int(input("Enter the Order quantity: "))
        count=0
        if check_quantity_available(item_order,item_quantity,vendor_items,vendor_items_quantity,count)==True:
            count=count+1
            
            if check_quantity_available(item_order,item_quantity,vendor_items,vendor_items_quantity,count)==True:
                count=count+1
                print(f'{item_order} is available.')
                index=vendor_items.index(item_order)
                check_quantity(index,item_quantity,vendor_items_quantity)
            else:
                print(f'{item_order} stock is over.')
        else:
            print(f'{item_order} is not available.')
        
    
# Vendor's Menu

vendor_menu_quantity = int(input("Enter the Size of the Menus:- "))
vendor_items=list(map(str, input("Enter Vendor Items:-  ").split()))
vendor_items_quantity=[]
for i in range(vendor_menu_quantity):
    
    quantity=int(input("Enter the Quantity:- "))
    vendor_items_quantity.append(quantity)

place_order(vendor_items,vendor_items_quantity)
    