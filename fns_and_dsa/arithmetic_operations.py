def perform_operation(num1, num2, operation):
    oper = ("add", "subtract", "multiply", "divide")
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
                if (num1 != 0) and (num2 != 0):
                    return num1 / num2
                elif num1 == 0 or num2 == 0:
                    return "Error : can,t divide by zero"
            
    return "Error: Invalid operation"