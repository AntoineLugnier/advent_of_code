with open('2021-31-05_Input.txt') as file:
    input = file.readlines()

smokeAreas = {}
multipleSmokeAreas = {}

for line in input :
    start, end = line.split(' -> ', 2)
    start = [int(pos) for pos in start.split(',')]
    end = [int(pos) for pos in end.split(',')]
    if start[0] == end[0] :

        xPos = start[0]

        if start[1] <= end[1] :
            yStart = start[1]
            yEnd = end[1]
        else :
            yStart = end[1]
            yEnd = start[1]

        for yPos in range (yStart, yEnd+1):
            pos = str(xPos) + '|' + str(yPos)
            if pos in smokeAreas:
                multipleSmokeAreas[pos] = True
            else :
                smokeAreas[pos] = True

    elif start[1] == end[1] :

        yPos = start[1]

        if start[0] <= end[0] :
            xStart = start[0]
            xEnd = end[0]
        else :
            xStart = end[0]
            xEnd = start[0]

        for xPos in range (xStart, xEnd+1):
            pos = str(xPos) + '|' + str(yPos)
            if pos in smokeAreas:
                multipleSmokeAreas[pos] = True
            else :
                smokeAreas[pos] = True

print(len(multipleSmokeAreas))
