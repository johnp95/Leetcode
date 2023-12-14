def sumOfDigits(n):
    if n < 1 : return 1
    remainder = n % 10
    return sumOfDigits(n//10) * remainder
if __name__ == '__main__':
   print(sumOfDigits(1342))