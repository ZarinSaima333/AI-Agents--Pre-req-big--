def chai_customer():
    print('welcome! what chai would you like?')
    order = yield #pause till send 
    while True:
        print(f'preparing: {order}') 
        #order= yield na thakle loop cholte thake masala chai er 
        order= yield
stall = chai_customer()
next(stall)#start the generator
stall.send('masala chai') #pass
#welcome! what chai would you like?
#preparing: masala chai

stall.send('lemon chai')
# welcome! what chai would you like?
# preparing: masala chai
# preparing: lemon chai