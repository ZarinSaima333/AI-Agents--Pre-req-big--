from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'Calling: {func.__name__}')
        result = func(*args,**kwargs)
        print(f'Finished: {func.__name__}')
    return wrapper

@log_activity
def brew_chai(type,milk="no"):
    print(f"Brewing {type} chai, whele milk status is {milk}")
brew_chai('masala')