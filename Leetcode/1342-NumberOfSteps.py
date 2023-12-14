def numberOfSteps(num):
    if num < 1 : return 0
    if num % 2 == 0 : 
        num /=2
    else:
        num -= 1
    return 1 + numberOfSteps(num)
    
if __name__ == '__main__':
    print(numberOfSteps(14)) # => 6