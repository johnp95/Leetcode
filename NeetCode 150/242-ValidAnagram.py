from collections import Counter
def isAnagram(s,t):
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        return s_counter == t_counter

s = 'anagram'
t = 'nagaram'

print(isAnagram(s,t))