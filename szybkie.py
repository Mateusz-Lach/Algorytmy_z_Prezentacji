def QuickSort(list, left, right):

    if left < right:
        i = left
        j = right

        pivot = list[(left + right) // 2]

        while True:
            while pivot > list[i]:
                    i += 1

            while pivot < list[j]:
                    j -= 1

            if i <= j:
                list[i], list[j] = list[j], list[i]
                i += 1
                j -= 1
            else:
                break
    
    if j > left:
            QuickSort(list, left, j)
    if i < right:
            QuickSort(list, i, right)


elements = [43, 52 ,6, 1, 7, 0, -54]

QuickSort(elements, 0, len(elements)-1)
print(*elements)


            