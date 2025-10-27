# arithmetic_operations.py (Module)
def perform_operation(num1, num2, operation):
    """a function that performs basic arithmetic operations"""
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Can't divide by Zero"
            return num1 / num2
