def square(number):
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    for n in range(number):
        number = 2 ** (number - 1) 
        return number
    
def total():
    total = 0
    for n in range(1,65):
        caca = 2 ** (n - 1) 
        total = total + caca
    return total
