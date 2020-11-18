number = input("List how many digits of the fibonacci sequence?\n")  # Gets user input
number = int(number)                # Converts user input to an integer

def fibonacci(n):                   # Function definition, returns the n-th fibonacci number
    x,y = 0,1                       # Declaring x and y
    if n == 0:                      # Conditional statement
        return x                    # Whitespace is important!
    if n == 1:                      # Conditional statement
        return y
    for z in range(1, n):           # Range creates a sequence of numbers from 1 to n
        x, y = y, x + y             # Set x to y, and y to x + y
    return y                        # Return y

fibNumbers = list()                 # Make a list called fibNumbers
for z in range (0, number):         # Invoke `fibonacci` n times
    fibNumbers.append(fibonacci(z)) # Append each result to the list

print(fibNumbers)                   # Print the result