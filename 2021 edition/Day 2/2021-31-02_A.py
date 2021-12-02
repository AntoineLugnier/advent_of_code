with open('2021-31-02_Input.txt') as file:
    input = file.readlines()

xValue = 0
yValue = 0

for value in input :
    data = value.split(' ')
    match data[0]:
        case "forward" :
            xValue += int(data[1])
        case "down" :
            yValue += int(data[1])
        case "up" :
            yValue -= int(data[1])

print(xValue * yValue)
