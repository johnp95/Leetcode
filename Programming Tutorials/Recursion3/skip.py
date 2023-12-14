def skipCharacter1(s,c,ans=''):
    if not s : return ans
    if s[0] != c:
        ans += s[0] 
    return skipCharacter1(s[1:],c,ans)
def skipCharacter2(s,c):
    if not s : return ''

    if s[0] != c:
        return s[0] + skipCharacter2(s[1:],c)
    return skipCharacter2(s[1:],c)
def skipWord(s,word):
    
    if not s : return ''
    if s.startswith(word):
        return skipWord(s[len(word):],word)
    return s[0] + skipWord(s[1:],word)
    
 
if __name__ == '__main__':
    s = 'baccad'

    # print(skipCharacter1(s,'a'))
    # print(skipCharacter2(s,'a'))
    print(skipWord('bcdapplejg','apple'))