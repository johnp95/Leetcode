from collections import defaultdict
def isAnagram(s,t):
    charFreq = defaultdict(int)
    for c in s:
        charFreq[c] += 1
    if len(s)==len(t):
        for c in t:
            if c in charFreq:
                charFreq[c] -= 1
            if charFreq[c] == 0:
                charFreq.pop(c)
            
        return True if not len(charFreq) else False 
    return False



if __name__ == '__main__':
    s = 'anagram'
    t = 'nagaram'
    # s = 'rat'
    # t = 'car'

    print(isAnagram(s,t))