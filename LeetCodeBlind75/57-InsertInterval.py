def insert(intervals,newInterval):
    # O(n)
    origLen = len(intervals)
    for i in range(len(intervals)):
        if newInterval[0] < intervals[i][0]:
            intervals.insert(i,newInterval)
            break
    if origLen ==len(intervals) : intervals.append(newInterval)
    output = [intervals[0]]
    for start,end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(end,lastEnd)
        else:
            output += [[start,end]]

    return output
        
    

if __name__ == '__main__':
    intervals,newInterval = [[1,3],[6,9]],[2,5]
    intervals,newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]
    intervals,newInterval = [],[4,8]
    intervals,newInterval = [[1,5]],[2,7]

    print(insert(intervals,newInterval))