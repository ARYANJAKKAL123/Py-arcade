#1 String Concatenation

def string_concat():

    first_word = "Game"
    second_word = "Dev"
    full_word = first_word + second_word
    print(f"Full word is: {full_word}")

#2 String Length

def string_length():
    string = "PythonProgramming"
    length = len(string)
    print(f"The length of the string is: {length}")

#3 String Slicing

def string_slicing():
    phrase = "Mastering Python"
    print(f"After slicing the string is the output: {phrase[10:]}")

#4 Negitive Indexing 

def negitive_indexing():
    text = "This is the simple message"
    print(f"Printing the last character of the string: {text[-1]}")

#5 Escaping Characters

def escpaing_char():
    text = "He said, \"Python is fun!\""
    print(text)

#6 Formatting with new line

def formatting_char():
    string = "Level 1 \n Start Game"
    print(string)

#7 Absolute Value and Round value

def absolute_and_round():
    n1 = -7.5
    n2 = 3.14159
    print(f"Printing the absolute value of the first number: {abs(n1)}")
    print(f"Printing the round value of the second number: {round(n2)}")

#8 Complex Numbers

def complex_numbers():
    number = complex(3,5)
    print(f"Printing the complex number: {number}")



def main():
    string_concat()
    string_length()
    string_slicing()
    negitive_indexing()
    escpaing_char()
    formatting_char()
    absolute_and_round()
    complex_numbers()

    
if __name__ == "__main__":
    main()
