def serve_chai():
    yield 'cup1: khanaz coffee'
    yield 'cup2: bel shorbot'
    yield 'cup3: lemonand'

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ['cup1','cup2','cup3']

def get_chai_gen():
    yield 'cup1'
    yield 'cup2'
    yield 'cup3'

chai = get_chai_gen()
print(chai) #<generator object get_chai_gen at 0x000001ED84A85C70> gen obj
print(next(chai)) # want the value cup1
print(next(chai))#cup2
print(next(chai))#cup3
print(next(chai))#error