oper = ("add", "subtract", "multiply", "divide")

def perform_operation(num1 , num2 , operation):
    validity = True if operation in oper else False
    
    if validity == True:
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                val = num1 / num2 if num2 != 0 else "Can't divide by zero"
                return val
        return f"{operation} is an invalid operation!"