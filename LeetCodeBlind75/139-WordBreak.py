def wordBreak(s,wordDict,memo={}):
<<<<<<< HEAD
    if s in memo : return memo[s]
    if s == '' : return True

    for word in wordDict:
        if s.startswith(word):
            if wordBreak(s[len(word):],wordDict,memo): 
                memo[s] = True
                return True

    memo[s] = False
    return False


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
=======
    if s in memo: return memo[s]
    if s == '':return True
    for i in wordDict:
        if s.startswith(i): 
            suffix = s[len(i):] 
            if wordBreak(suffix,wordDict):
                memo[s] = True
                return True
    memo[s] = False
    return False

if __name__ == '__main__':
    # s,wordDict = "leetcode",["leet","code"]
    # s,wordDict = "applepenapple", ["apple","pen"]
    # s,wordDict = "catsandog", ["cats","dog","sand","and","cat"]
    s,wordDict = "cars", ['car','ca','rs']
>>>>>>> 96a3263ee57dfe1c41053252a5346925f7219a48
    print(wordBreak(s,wordDict))