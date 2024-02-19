def characterReplacement(s,k):

    char_map = {}
    longest = 0
    start = 0
    for end in range(len(s)):
        
        char_map[s[end]] = 1 + char_map.get(s[end],0)
        if (end - start + 1) - max(char_map.values()) > k:
            char_map[s[start]] -= 1
            start += 1
        longest = max(longest,end - start + 1)
    return longest
        
        
s = "AABABBA"
s = "ABABBA"
s = "ABABAAAABBBBBBBBB"
print(characterReplacement(s,1))