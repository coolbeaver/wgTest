def isEven(value):
    nor_array = ['0', '2', '4', '6', '8']
    if str(value)[-1] in nor_array:
        return True
    else:
        return False


print(isEven(123))
