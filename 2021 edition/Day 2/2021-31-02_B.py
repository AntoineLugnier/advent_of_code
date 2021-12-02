with open('2021-31-02_Input.txt') as file:
    input = file.readlines()

xValue = 0
yValue = 0
aim = 0

for value in input :
    data = value.split(' ')
    match data[0]:
        case "forward" :
            xValue += int(data[1])
            yValue += int(data[1]) * aim
        case "down" :
            aim += int(data[1])
        case "up" :
            aim -= int(data[1])

print(xValue * yValue)
