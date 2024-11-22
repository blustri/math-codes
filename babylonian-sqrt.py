##    sqrt_counter   ##
squaresLimit = 20 # limit how many times to calculate perfect squares
# perfect square list #
squares = [] # value form (1, 4, 9...)
perf_sq = [] # number form (x^y)
number = 1
for number in range(1, squaresLimit + 1):
    squares.append(number * number)
    perf_sq.append(number)
## babylonian method to find square roots ##
try:
    targetNumber = int(input("What value to use? : "))
except ValueError:
    print("input number above 0!")
    exit()
seen = [] # we use this to iterate through every number in squares[] - targetNumber
for i in squares:
    if i < targetNumber: # this will make sure to only use the numbers BELOW our target number, so that we can match the Babylonian method for sqrt
        temp = abs(int(targetNumber) - i)
        seen.append(temp)
    else:
        continue
closestTarget = min(seen) # takes the lowest number in the seen[] array
index = seen.index(closestTarget) # uses the lowest number in seen[] array to find its index in our perfect square list
psToUse = perf_sq[index] # takes the closest square root number (condition: not above the input)
valueToUse = squares[index] # takes the squared value (not its root number)
# calculation #
sqrt = psToUse
for i in range(3): # repeats the calculations 3 times to get an accurate estimate
    sqrt = (sqrt + targetNumber / sqrt) / 2
## output ##
print(f"perfect square to use, paired with its value = ({psToUse}, {valueToUse})") # number to use
print(f"the square root of {targetNumber} is {sqrt}") # answer