with open('2021-31-01_Input.txt') as file:
    input = file.readlines()

numberOfIncreases = 0
currentValue = None

for value in input :
    if not currentValue is None :
        if int(currentValue) < int(value) :
            numberOfIncreases += 1
    currentValue = value

print(numberOfIncreases)
