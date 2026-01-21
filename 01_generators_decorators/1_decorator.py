#wrappwer around your func preserves meta data

from functools import wraps 
def my_decorator(func):
    @wraps(func) #new ,now greet
    def wrapper():
        print("before func")
        func()
        print('after func runs')
    return wrapper

@my_decorator #na dile just hello
def greet(): #greet will be wrapped up
    print("helooo")

greet()
print(greet.__name__)#wrapper changes the metadata so use built in library
#before func
# helooo
# after func runs