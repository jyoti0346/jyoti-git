

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
number = int(input("Enter a number: "))
result = even_odd(number)
print("The number is", result)