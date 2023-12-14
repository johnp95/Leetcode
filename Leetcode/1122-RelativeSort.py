def relativeSortArray(arr1,arr2):
    n = len(arr2)
    d = {}
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            d[arr1[i]] = arr2.index(arr1[i])
        else:
            d[arr1[i]] = n
    sorted_d = dict( sorted( d.items(), key=lambda x: (x[1],x[0])) )
    ans = []
    for i,j in sorted_d.items():
        ans += [i] * arr1.count(i)
    return ans
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1,arr2))