def uniquePaths(m,n,memo={}):
    if (m,n) in memo : return memo[(m,n)]
    if m == 1 or n == 1 : return 1
    if m == 0 or n == 0 : return 0

    memo[(m,n)] =  uniquePaths(m-1,n) + uniquePaths(m,n-1)
    return memo[(m,n)]


if __name__ == '__main__':
    print(uniquePaths(30,72))