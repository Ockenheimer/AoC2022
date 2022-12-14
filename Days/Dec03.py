file = open("input03", "r")
summe = 0

for line in file.read().splitlines():
    front = line[:len(line) // 2]
    back = line[len(line) // 2:]

    for i in range(0, len(front)):
        for j in range(0, len(back)):
            if front[i] == back[j]:
                if front[i].isupper():
                    summe += ord(front[i]) - 38
                else:
                    summe += ord(front[i]) - 96
                break
        if front[i] == back[j]:
            break

file.close()

file = open("input03", "r")
rucksacks = []
for line in file.read().splitlines():
    rucksacks.append(line)

groupBatch = 0
group0 = 0
group1 = 1
group2 = 2
safe = 0
while group0 < len(rucksacks):
    for i in range(0, len(rucksacks[group0])):
        for j in range(0, len(rucksacks[group1])):
            if rucksacks[group0][i] == rucksacks[group1][j]:
                for k in range(0, len(rucksacks[group2])):
                    if rucksacks[group0][i] == rucksacks[group2][k]:
                        if rucksacks[group0][i].isupper():
                            if safe == 0:
                                groupBatch += ord(rucksacks[group0][i]) - 38
                                safe = 1
                                print(group0)
                                # print(groupBatch)
                                break
                        else:
                            if safe == 0:
                                groupBatch += ord(rucksacks[group0][i]) - 96
                                safe = 1
                                print(group0)
                                # print(groupBatch)
                                break
                if rucksacks[group1][j] == rucksacks[group2][k]:
                    break
            if rucksacks[group0][i] == rucksacks[group1][j]:
                break

    group0 += 3
    group1 += 3
    group2 += 3
    safe = 0

print(summe)
print(groupBatch)
