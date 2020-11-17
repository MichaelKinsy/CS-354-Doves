print("Power digit sum.")
bInput = input("Enter base. > ")
eInput = input("Enter exponential. > ")

def powerdigitsum(int base, int exp):
    result = math.pow(base,exp)
    sum = 0
    digit = 0
    while(result != 0):
        digit = result % 10 #add right most digit in result to digit
        sum += digit
        result = result / 10 #remove right most digit in result
    return sum

powerdigitsum = [] #Make a list called powerdigitsum
powerdigitsum.append(powerdigitsum(bInput,eInput)) # Append result to powerdigitsum
print(powerdigitsum) #Print the result
