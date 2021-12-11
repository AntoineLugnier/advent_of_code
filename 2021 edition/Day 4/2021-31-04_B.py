# FUNCTIONS
def checkCompleteBingo (bingo):
    keys = list(bingo)
    return max(
        sum([bingo[keys[0]], bingo[keys[1]], bingo[keys[2]], bingo[keys[3]], bingo[keys[4]]]),
        sum([bingo[keys[5]], bingo[keys[6]], bingo[keys[7]], bingo[keys[8]], bingo[keys[9]]]),
        sum([bingo[keys[10]], bingo[keys[11]], bingo[keys[12]], bingo[keys[13]], bingo[keys[14]]]),
        sum([bingo[keys[15]], bingo[keys[16]], bingo[keys[17]], bingo[keys[18]], bingo[keys[19]]]),
        sum([bingo[keys[20]], bingo[keys[21]], bingo[keys[22]], bingo[keys[23]], bingo[keys[24]]]),
        sum([bingo[keys[0]], bingo[keys[5]], bingo[keys[10]], bingo[keys[15]], bingo[keys[20]]]),
        sum([bingo[keys[1]], bingo[keys[6]], bingo[keys[11]], bingo[keys[16]], bingo[keys[21]]]),
        sum([bingo[keys[2]], bingo[keys[7]], bingo[keys[12]], bingo[keys[17]], bingo[keys[22]]]),
        sum([bingo[keys[3]], bingo[keys[8]], bingo[keys[13]], bingo[keys[18]], bingo[keys[23]]]),
        sum([bingo[keys[4]], bingo[keys[9]], bingo[keys[14]], bingo[keys[19]], bingo[keys[24]]]))

def getBingoValue (bingo) :
    total = 0
    for key, value in bingo.items():
        if key != 'countdown':
            if not value :
                total += key
    return total

# MAIN
with open('2021-31-04_Input.txt') as file:
    input = file.read()

data = input.split('\n\n')

pullOrder = [int(number) for number in data[0].split(',')]

bingosList = []

for bingoId in range (1, len(data)) :
    bingo = {}
    for line in data[bingoId].split("\n") :
        if not line :
            break
        bingo |= {
            int(line[0:2].strip()) : 0,
            int(line[3:5].strip()) : 0,
            int(line[6:8].strip()) : 0,
            int(line[9:11].strip()) : 0,
            int(line[12:14].strip()) : 0}
    bingo |= {'countdown' : 5}
    bingosList.append(bingo)

returnValue = 0

for pullValue in pullOrder :
    if not returnValue :
        numberOfBingo = 0
        for bingo in bingosList :
            if bingo['countdown'] >= 0 :
                numberOfBingo += 1
                if pullValue in bingo :
                    bingo[pullValue] = 1
                    bingo['countdown'] -= 1
                    if not bingo['countdown'] :
                        bingo['countdown'] = 5 - checkCompleteBingo(bingo)
                        if not bingo['countdown'] :
                            bingo['countdown'] = -1
                            returnValue = pullValue * getBingoValue(bingo)

        if numberOfBingo == 1 and returnValue :
            break
        else :
            returnValue = 0

print(returnValue)
