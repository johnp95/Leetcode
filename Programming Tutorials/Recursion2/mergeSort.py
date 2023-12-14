def merge(data,start,mid,end):
    temp = [0]*(end-start+1)
    i,j,k = start,mid+1,0

    while i <= mid and j<=end:
        if data[i]<= data[j]:
            temp[k] = data[i]
            i += 1
            k +=1
        else:
            temp[k] = data[j]
            k += 1
            j += 1
    while i <= mid:
        temp[k] = data[i]
        k += 1
        j +=1
    while j <= end:
        temp[k] = data[j]
        k +=1
    for i in range(len(end)+1):
        data[i] = temp[i-start]

def mergeSort(data,start,end):
    if start < end:
        mid = (start+end)//2
        mergeSort(data,start,mid)
        mergeSort(data,mid+1,end)
        merge(data,start,mid,end)

data = [-5,20,10,3,2,0]
print(mergeSort(data,0,len(data)-1))