from collections import Counter

def topKFrequent(nums,k):
  
    count = Counter(nums)
    freq = [[] for _ in range(len(nums) + 1)]
    print(freq)

    for n,c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
nums = [1,1,1,2,2,3,8,8,8,8,8,8]
k = 2
print(topKFrequent(nums,k))