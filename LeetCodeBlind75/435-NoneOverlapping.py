def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[0])
    merge = []
    merge += [intervals[0]]
    ans = 0
    idx = []
    for start,end in intervals[1:]:
        if start < merge[-1][1]:
            ans +=1
            if end < merge[-1][1]:
                idx = [[start,end]]
            else:
                idx = merge
        else:
            idx = [[start,end]]            
        merge = idx
            
    return ans
if __name__ == '__main__':
    interval0 = [[1,2],[2,3],[3,4],[1,3]]
    interval1 = [[1,2],[1,2],[1,2]]
    interval2 = [[1,2],[2,3]]
    interval3 = [[1,100],[11,22],[1,11],[2,12]]
    intervals = [interval0,interval1,interval2,interval3]
    outputs = [1,2,0,2]
    for i,test in enumerate(intervals):
        print(test,eraseOverlapIntervals(test)==outputs[i])
