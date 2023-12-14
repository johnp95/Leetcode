def isPalindrome(input):
    if len(input)==0 or len(input) == 1: return True

    if input[0] == input[-1]:
        return isPalindrome(input[1:-1])
    return False
print(isPalindrome('kayak'))