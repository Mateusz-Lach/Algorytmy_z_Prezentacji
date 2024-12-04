def BubbleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                helper = list[j]
                list[j] = list[j+1]
                list[j+1] = helper
    return list

elements = [54, 23, 5, 1, 6, 3]

print(BubbleSort(elements))