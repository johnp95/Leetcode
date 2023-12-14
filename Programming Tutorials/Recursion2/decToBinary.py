#my way
def findBinary(decimal,result=''):
    if decimal == 0 :return result
    return findBinary(decimal//2,result) + str(decimal%2)
def find_binary(decimal, result=""):
    if decimal == 0:
        return result

    result = str(decimal % 2) + result
    return find_binary(decimal // 2, result)

print(findBinary(4))
# print(find_binary(233))
