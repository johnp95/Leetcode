def reverse(n,_sum=0):
    if n==0:
        return _sum
    rem = n % 10
    _sum = _sum * 10 + rem
    return reverse(n//10,_sum)


if __name__ == '__main__':
    print(reverse(12345) )# => 54321