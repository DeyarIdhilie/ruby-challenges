'''
challenge 1
Fibonacci challenge
Challenge:
A Fibonacci Sequence is created by adding two numbers to create the next number in the sequence.
You then sum that number with the one preceding it to get the next number,, and so on.
For example, if you have the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, then the next number in the sequence is 55.
'''

def find_next_number_in_sequence():
    sequence = input("Please enter the sequence: ")
    split_sequence = sequence.split(',')
    next_number_in_sequence = int(split_sequence[-2].replace(" ","")) + int(split_sequence[-1].replace(" ",""))
    print("The next number in the sequence will be: ", next_number_in_sequence)

def fibonacci_sequence():
    n = int(input("Enter an integer: "))
    sequence = []
    a, b = 0, 1 #the first nubmer in sequence is 0# the 2nd number is 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    print(sequence)


def get_choice():
    choice = input()
    if choice == '1':
        find_next_number_in_sequence()
    elif choice == '2':
        fibonacci_sequence()


def print_choices():
    print("Choose what you want:\n"
          "1. Find the next number in the sequence\n"
          "2. Enter a number and return the fibonnaci sequence \n")

print_choices()
get_choice()