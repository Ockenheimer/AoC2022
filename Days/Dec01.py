file = open("days/input01", "r")
dwarfs = []
summe = 0
for line in file.read().splitlines():
    if line.isnumeric():
        summe += int(line)
    else:
        dwarfs.append(summe)
        summe = 0

dwarfs.sort()
print(dwarfs[len(dwarfs) - 1] + dwarfs[len(dwarfs) - 2] + dwarfs[len(dwarfs) - 3])
