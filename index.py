

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
number = 5
result = even_odd(number)
print("The number is", result)