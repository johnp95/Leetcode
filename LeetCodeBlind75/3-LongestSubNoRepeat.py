from collections import defaultdict
def lengthofLongestSubstring(s):
    long = float('-inf')
    start = 0
    charFrequency = defaultdict(int)
    for end in range(len(s)):
        charEnd = s[end]
        charFrequency[charEnd] += 1

        while charFrequency[charEnd] > 1:
            charStart = s[start]
            charFrequency[charEnd] -= 1
            start += 1
        long = max(long,end-start+1)
    return long


if __name__ == '__main__':
    print(lengthofLongestSubstring('abcabcbb'))
    print(lengthofLongestSubstring('bbbbb'))
    print(lengthofLongestSubstring('pwwkew'))