def lengthOfLongestSubstring(s):
    
    longest,start = 0,0

    char_set = set()

    for end in range(len(s)):
        while s[end] in char_set:
            c = s[start]
            char_set.remove(c)
            start += 1
    
        char_set.add(s[end])

        longest = max(longest,end-start+1)
    return longest

s = "abcabcbb" # -> 3
# s = "pwwkew" # -> 3
res = lengthOfLongestSubstring(s)
print(res)