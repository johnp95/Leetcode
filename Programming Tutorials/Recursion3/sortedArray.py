def sortedArray(arr):
    if not  len(arr)  : return True

    return arr[0] < arr[-1] and sortedArray(arr[1:-1])

if __name__ == '__main__':
    arr = [1,2,4,8,9,12] # -> True
    arr = [1,2,4,3,8,9] # => False
    print(sortedArray(arr))