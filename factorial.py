#5! = 5 * 4 * 3 * 2 * 1 = 120

# Input number as num from user
num = int(input("Enter a number to calulate its factorial: "))

# initialise i = 1
i = 1
# initialise fact = 1
fact = 1

# loop until i <= num
while i <= num:
    # fact = fact * i
    fact = fact * i
    #i = i + 1
    i = i + 1

# display fact
print(fact)