def InsertionSort(list):
    for i in range(1, len(list)):
        helper = list[i]
        j = i-1
        while j >= 0 and list[j] > helper:
            list[j + 1] = list[j]
            j = j -1
        list[j + 1] = helper
    return list

elements = [5, 4, 2, 7, 65, -8, 256]

print(InsertionSort(elements))