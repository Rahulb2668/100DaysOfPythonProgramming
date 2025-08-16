def add(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return  n1*n2

def divide(n1,n2):
    return n1/n2

def substract(n1, n2):
    return n1 - n2


def my_calculator():
    first_number = None
    continue_calculation = True
    while continue_calculation:
        if first_number is None:
            first_number = int(input("What is your first Number? "))

        operator = input("Select Your Operator: x\n +\n -\n /\n")

        second_number = int(input("Whats your second number ?"))
        result = 0
        match operator:
            case "+":
                result = add(first_number, second_number)

            case "-":
                result = substract(first_number, second_number)

            case "/":
                result = divide(first_number, second_number)

            case "*":
                result = mul(first_number, second_number)


        print(f"Your answer is {result}")
        user_decision = input("Would you like to continue with result enter 'y' or 'n' for would you like to start a new calculation")

        if user_decision.lower() == "y":
            first_number = result
        elif user_decision.lower() == "n":
            first_number = None
        else:
            continue_calculation = False



my_calculator()