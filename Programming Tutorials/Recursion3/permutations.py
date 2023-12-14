def perm(s,current='',idx=0):
    if idx == len(s):
        return [current]
    ans = []
    for i in range(idx+1):
        ans +=  perm(s,current[:i] + s[idx] + current[i:],idx+1)
    return ans

def permCount(s,current='',idx=0):
    if idx == len(s):
        return 1
    count = 0
    for i in range(idx+1):
        count +=  permCount(s,current[:i] + s[idx] + current[i:],idx+1)
    return count


if __name__ == '__main__':
    s = 'abc'
    print(perm(s))