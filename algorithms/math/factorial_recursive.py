#Calculate factorial of a given number using recursive method.

def factorial(number):

    return 1 if number in [0, 1] else number * factorial(number - 1)

if __name__ == '__main__':

    enter_number = int(input("Enter a number whose factorial is required : "))
    result = factorial(enter_number)
    print(result)