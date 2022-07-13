def quickSort(array):
    if len(array) < 2:
        return array
    else:
        base = array[0]
        low = [i for i in array[1:] if i < base]
        high = [i for i in array[1:] if i > base]
        return quickSort(low) + [base] + quickSort(high)


print(quickSort([6, 2, 4, 5]))
