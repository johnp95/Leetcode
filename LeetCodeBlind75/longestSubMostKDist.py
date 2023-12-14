from collections import defaultdict

def disChar(s, k):
    start,end = 0,0
    long = k
    freq = defaultdict(int)
    while end < len(s):
        freq[s[end]] += 1

        if len(freq) > k:
            long = max(long,end-start)
            freq[s[start]] -= 1
            if freq[s[start]]==0:
                freq.pop(s[start])
            start += 1
        end +=1
    print(dict(freq),len(freq),sum(freq.values()))
    return long


if __name__ == '__main__':
   
    print(disChar('abcefg',1))
    print(disChar('aaaaaaaa',3))
    
 