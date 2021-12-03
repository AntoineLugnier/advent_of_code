with open('2021-31-03_Input.txt') as file:
    input = file.readlines()

valuesCounting = {}

for value in input :
    pos = 0
    for bit in value :
        if bit in ["0", "1"] :
            pos += 1
            if not pos in valuesCounting :
                valuesCounting[pos] = {"0": 0, "1": 0}
            valuesCounting[pos][bit] += 1

gammaRate = ""
epsilonRate = ""

for pos, counting in valuesCounting.items() :
    if counting["0"] < counting["1"] :
        gammaRate += "1"
        epsilonRate += "0"
    else :
        gammaRate += "0"
        epsilonRate += "1"

print(int(gammaRate, 2) * int(epsilonRate, 2))
