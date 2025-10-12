def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper
    

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")
    
get_ice_cream("vanilla")
"""
para conseguir passar um argumento como flavor para get_ice_cream,
você precisa definir o *args, **kwargs tanto em wrapper quanto em func, em todas as 
@add que você for usar"""

