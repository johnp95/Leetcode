def numZeros(n,count=0):
    if n < 1 : return count

    rem = n%10
    if rem == 0: 
        count += 1
    return numZeros(n//10,count)
    




if __name__ == '__main__':
    print(numZeros(30204))