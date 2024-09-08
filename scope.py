# Scope - global and local

fname = "John"
lname = "Smith"

# Pure function
def greet():
    fname = "first"
    lname = "last"
    print(fname)
    print(lname)

greet()
print(fname)
print(lname)
