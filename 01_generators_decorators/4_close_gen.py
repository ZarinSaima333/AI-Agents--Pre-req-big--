def local_chai():
    yield 'masala chai'
    yield 'Ginger Chai'


def imported_chai():
    yield 'matcha'
    yield 'Oolong'

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

# masala chai
# Ginger Chai
# matcha     
# Oolong 

def chai_stall():
    try:
        while True:
            order= yield "waiting for chai order"
    except:
        print('tsall closed no more chai')

stall = chai_stall()
print(next(stall))
#masala chai
# Ginger Chai
# matcha
# Oolong
# waitinf for chai order
# tsall closed no more chai
stall.close() #exit and clean
# masala chai
# Ginger Chai
# matcha
# Oolong
# waitinf for chai order
# tsall closed no more chai