list1 = []
list2 = []

with open('./input.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        numbers = [int(num) for num in numbers]
        list1.append(numbers[0])
        list2.append(numbers[1])

list1 = sorted(list1)
list2 = sorted(list2)

total = 0
for i in range(len(list1)):
    difference = abs(list1[i] - list2[i])
    total += difference

print(total)