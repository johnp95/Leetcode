def avgSub(nums,k):
    # approach 1
    # ans = []
    # for i in range(len(nums)-k+1):
    #     ans += [sum(nums[i:i+k])//k]
    # return ans

    # approach 2

    s,e = 0,0
    ans = []
    curr_sum = 0
    while e < len(nums):
        curr_sum += nums[e]
        if e - s + 1 == k:
            ans += [curr_sum / (e-s+1)]
            curr_sum -= nums[s]
            s += 1
        e += 1

    return ans
def smallestSub(nums,s):
    start,end,currSum = 0,0,0
    min_length = float('inf')
    while end < len(nums):
        currSum += nums[end]
        while  currSum >= s:
            currSum -= nums[start]
            min_length = min(min_length,end-start+1)
            start += 1
        end += 1
    
    return min_length
def longest_sub_kDistinct(s,k):
    windowStart,windowEnd = 0,0
    letterFrequencies = {}
    longestSubstrSoFar = 0

    # for windowEnd in range(len(s)):
    while windowEnd < len(s):
        windowEndChar = s[windowEnd]

        if windowEndChar not in letterFrequencies:
            letterFrequencies[windowEndChar] = 0
        letterFrequencies[windowEndChar] += 1

        while len(letterFrequencies) > k:
            windowStartChar = s[windowStart]
            letterFrequencies[windowStartChar] -= 1
            if letterFrequencies[windowStartChar] == 0:
                del letterFrequencies[windowStartChar]
            windowStart += 1

        longestSubstrSoFar = max(longestSubstrSoFar,windowEnd-windowStart+1)
        windowEnd +=1
    return longestSubstrSoFar





if __name__ == '__main__':
    print(longest_sub_kDistinct('acccpbbebi',3))
    print(longest_sub_kDistinct('aaaaaaaa',3))
