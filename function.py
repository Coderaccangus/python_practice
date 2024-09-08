# Define the function that greets the user
def greet(fname, lname):
    print(f"Hello {fname} {lname}")

# Get user input for first and last names
user_input = input("Please enter your first and last name: ")

# Split the input into first and last names
# Assuming the input is always two words separated by a space
first_name, last_name = user_input.split()

# Call the function with the split names
greet(first_name, last_name)
