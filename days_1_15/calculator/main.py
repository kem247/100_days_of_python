from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc_dictionary = {"+": add, "-": subtract,
                   "*": multiply, "/": divide,
                   }


def calc_function():
    should_accumulate = True
    first_number = input("What's the first number?: ")
    while should_accumulate:
        if first_number:
            op_arr = list(calc_dictionary.keys())
            op_str = '\n'.join(str(x) for x in op_arr)
            print(op_str)
            operation = input("Pick an operation: ")
            second_number = input("What's the next number?: ")
            result = float(calc_dictionary[operation](int(first_number), int(second_number)))
            print(f"{float(first_number)}" + f" {operation}" + f" {float(second_number)}" + f" = {result}")
            choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            if choice == "y":
                first_number = result
            else:
                should_accumulate = False
                print("\n" * 20)
                print(logo)
                calc_function()
    else:
        return


calc_function()
