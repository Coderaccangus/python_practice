#if we want to create a function to say whether a number is odd or even












input = int(input("Please enter a number: "))



def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(input)