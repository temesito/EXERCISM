def is_armstrong_number(number):
    total = 0
    exponent = len(str(number))
    for digit in str(number):
        total += int(digit) ** exponent

    return total == number
    
        
