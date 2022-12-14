file = open("days/input02", "r")

summe = 0
summe2 = 0
# outcome = ""

for line in file.read().splitlines():
    choice = line.split(" ")
    if choice[1] == "X":
        if choice[0] == "A":
            summe += 4
        else:
            if choice[0] == "B":
                summe += 1
            else:
                summe += 7
    if choice[1] == "Y":
        if choice[0] == "A":
            summe += 8
        else:
            if choice[0] == "B":
                summe += 5
            else:
                summe += 2
    if choice[1] == "Z":
        if choice[0] == "A":
            summe += 3
        else:
            if choice[0] == "B":
                summe += 9
            else:
                summe += 6
file.close()

file = open("days/input02", "r")

for line in file.read().splitlines():
    choice = line.split(" ")
    if choice[1] == "X":  # LOSE
        if choice[0] == "A":
            summe2 += 3
        else:
            if choice[0] == "B":
                summe2 += 1
            else:
                summe2 += 2
    if choice[1] == "Y":  # DRAW
        if choice[0] == "A":
            summe2 += 4
        else:
            if choice[0] == "B":
                summe2 += 5
            else:
                summe2 += 6
    if choice[1] == "Z":  # WIN
        if choice[0] == "A":
            summe2 += 8
        else:
            if choice[0] == "B":
                summe2 += 9
            else:
                summe2 += 7
file.close()
print(summe)
print(summe2)
