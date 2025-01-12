def perform_operation(num1, num2, operation):
    oper = ("add", "subtract", "multiply", "divide")
    validity = True if operation in oper else False
    
    if num2 == 0 and operation == "divide":
            return "Error: can't divide by zero"
    elif validity == True:
            match operation:
                case "add":
                    return num1 + num2
                case "subtract":
                    return num1 - num2
                case "multiply":
                    return num1 * num2
                case "divide":
                    return num1 / num2
                
    return "Error: Invalid operation"