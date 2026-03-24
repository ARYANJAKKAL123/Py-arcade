# 1 Basic Arithmetic
def basic_arithmetic():
    num1 = 10
    num2 = 3
    result = num1 // num2
    print(f"The numbers are: {num1} and {num2}")
    print(f"Floor division using '//' operator: {result}")


# 2 Exponents and Remainders
def exponents_and_remainders():
    number1 = 2
    number2 = 8
    power = number1 ** number2
    remainder = number1 % number2
    print(f"The numbers are: {number1} and {number2}")
    print(f"The power of the numbers: {power}")
    print(f"The remainder of the numbers: {remainder}")


# 3 Combined Assignment Shorthand
def combined_assignment():
    experience_level = 100
    experience_level += 50
    print(f"Experience level after += 50: {experience_level}")


# 4 Comparison Operators
def comparison_operators():
    a = 15
    b = 20
    print(f"Checking if 'a' is not equal to 'b': {'True' if a != b else 'False'}")


# 5 Logical Operators (and / or)
def logical_operators():
    has_key = True
    is_locked = False
    result = False 

    if has_key == True and is_locked == False:
        result = True

    print(f"The result of the condition is: {result}")

#6 Boolean "Falsy Logic"

def boolean_Falsy_Logic():
    result = "" or "Default"
    print(f"The results is: {result}")

#7 Membership and Identity

def check_presence():
    List = ['a','b','c']
    print("True" if 'p' in List else "False")

#8 The Ternary Operator

def ternary_operator():
    score = 100
    status = "Winner" if score>=100 else "Try Again"
    print(f"The Status is: {status}")

def main():
    basic_arithmetic()
    exponents_and_remainders()
    combined_assignment()
    comparison_operators()
    logical_operators()
    boolean_Falsy_Logic()
    check_presence()   
    ternary_operator()


if __name__ == "__main__":
    main()
