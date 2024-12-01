file = open("day1/input.txt", "r")

list1 = []
list2 = []
for line in file:
    line_content = line.split()
    list1.append(int(line_content[0]))
    list2.append(int(line_content[1]))

list1.sort()
list2.sort()

total = 0
for index in range(0, len(list1)):
    total += abs(list1[index] - list2[index])

print(total)