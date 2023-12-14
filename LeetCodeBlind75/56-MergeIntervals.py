def merge(intervals):
    intervals = sorted(intervals,key=lambda x: x[0])
    merge = []
    merge += [intervals[0]]
    ans = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] <= merge[0][1]:
            merge = [[merge[0][0], max(intervals[i][1],merge[0][1])]]
            ans.pop()
            ans += merge
        else:
            merge = [intervals[i]]
            ans += [intervals[i]]
    return ans
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    print(merge(intervals))