number = int(input("Type a Number: "))

def num_class(number):
    if (number % 2) == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")