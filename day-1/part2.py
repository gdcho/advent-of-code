list1 = []
list2 = []

with open('./input.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        numbers = [int(num) for num in numbers]
        list1.append(numbers[0])
        list2.append(numbers[1])


def freq_set(lst, bad):
    freq = {}
    for num in lst:
        if num in bad:
            continue
        elif num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    return freq


bad_items = []
combined = freq_set(list1 + list2, bad_items)
for key in combined.keys():
    if combined[key] == 1:
        bad_items.append(key)

freq1 = freq_set(list1, bad_items)
freq2 = freq_set(list2, bad_items)


ANS = 0
for key in freq1.keys():  
    ANS += freq1[key] * freq2[key] * key
print(ANS)