from collections import Counter
def checkInclusion(s1,s2):
    s1_map = Counter(s1)
    s2_map = Counter()

    if len(s1) > len(s2):
        return False

    start = 0
    for end in range(len(s2)):
        s2_map[s2[end]] += 1
        if end >= len(s1):
            if s2_map[s2[start]] > 1:
                s2_map[s2[start]] -= 1                    
            else:
                del s2_map[s2[start]]
            start += 1
        if s1_map == s2_map:
            return True 

    return False
s1 = "ab"
s2 = "eeidbaooo"
print(checkInclusion(s1,s2))