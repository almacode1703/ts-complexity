def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for i in range(len(binary_str) - 1, -1, -1):
        decimal += int(binary_str[i]) * (2 ** power)
        power += 1
    return decimal

# Test Case 1
binary1 = input("Enter your Binary: ")
print("Decimal : ", binary_to_decimal(binary1))
print()

# Test Case 2
binary2 = input("Enter your Binary: ")
print("Decimal : ", binary_to_decimal(binary2))