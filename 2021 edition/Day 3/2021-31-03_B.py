with open('2021-31-03_Input.txt') as file:
    input = file.readlines()

firstGammaValue = None
firstEpsilonValue = None
gammaRate = ""
epsilonRate = ""

for bit in input[0]:

    if bit in ("0", "1") :

        gammaCount = {"0" : 0, "1" : 0}
        epsilonCount = {"0" : 0, "1" : 0}

        for value in input :
            if gammaRate + "0" == value[0:len(gammaRate)+1] :
                firstGammaValue = value
                gammaCount["0"] += 1
            elif gammaRate + "1" == value[0:len(gammaRate)+1] :
                firstGammaValue = value
                gammaCount["1"] += 1

            if epsilonRate + "0" == value[0:len(epsilonRate)+1] :
                firstEpsilonValue = value
                epsilonCount["0"] += 1
            elif epsilonRate + "1" == value[0:len(epsilonRate)+1] :
                firstEpsilonValue = value
                epsilonCount["1"] += 1

        if gammaCount["1"] + gammaCount["0"] > 1 :
            if gammaCount["1"] >= gammaCount["0"] :
                gammaRate += "1"
            else :
                gammaRate += "0"
        else :
            gammaRate += firstGammaValue[len(gammaRate)]

        if epsilonCount["1"] + epsilonCount["0"] > 1 :
            if epsilonCount["1"] < epsilonCount["0"] :
                epsilonRate += "1"
            else :
                epsilonRate += "0"
        else :
            epsilonRate += firstEpsilonValue[len(epsilonRate)]

print(int(gammaRate, 2) * int(epsilonRate, 2))
