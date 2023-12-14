def wordBreak(s,wordDict,memo={}):
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
    print(wordBreak(s,wordDict))