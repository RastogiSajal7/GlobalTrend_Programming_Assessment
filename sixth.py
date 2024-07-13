def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero. Please provide a non-zero denominator."
num = float(input("Enter the numerator: "))
den = float(input("Enter the denominator: "))
result = safe_divide(num, den)
print(f"The result of the division is: {result}")
