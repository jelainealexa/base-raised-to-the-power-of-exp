# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

# Write the function
def exponent(base, exp):
    result = 1
    # Multiply base by itself n times
    for i in range(exp):
        result *= base

    return result

# Given
base_number = 15
exponent_number = 3

# Result value
result = exponent(base_number, exponent_number)

# Print result
print(f"{base_number} raised to the power of {exponent_number} is {result}")