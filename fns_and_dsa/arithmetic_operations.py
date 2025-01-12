def perform_operation(num1 , num2 , operation):
    def valid(operation):
        oper = ("add", "subtract", "multiply", "divide")
        return True if operation in oper else False
    
    if valid(operation) == True:
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
    else:
        print(f"{operation} is an invalid operation!")