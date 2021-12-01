with open('2021-31-01_Input.txt') as file:
    input = file.readlines()

numberOfIncreases = 0
previousValue = None

for key in range (0, len(input)-2) :
    currentValue = int(input[key]) + int(input[key+1]) + int(input[key+2])
    if not previousValue is None :
        if previousValue < currentValue :
            numberOfIncreases += 1
    previousValue = currentValue
    
print(numberOfIncreases)
