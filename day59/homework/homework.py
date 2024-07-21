def matematik(string_number, number):
    try:
        # Convert the string to a number
        string_number = float(string_number)
        
        # Perform arithmetic operations
        addition = string_number + number
        subtraction = string_number - number
        multiplication = string_number * number
        division = string_number / number if number != 0 else "Undefined (division by zero)"

        # Print the results
        print(f"Addition: {string_number} + {number} = {addition}")
        print(f"Subtraction: {string_number} - {number} = {subtraction}")
        print(f"Multiplication: {string_number} * {number} = {multiplication}")
        print(f"Division: {string_number} / {number} = {division}")
        
    except ValueError:
        print("The provided string could not be converted to a number.")

# Example usage
arithmetic_operations("10", 5)
arithmetic_operations("20.5", 2.5)
arithmetic_operations("abc", 3)
