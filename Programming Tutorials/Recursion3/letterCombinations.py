def letterCombo(digits,curr='',idx=0):
    if idx == len(digits):
        return [curr] if curr else []
    ans = []
    digit = int(digits[idx])
    x = 0 if digit < 7 or digit == 8 else 1
    for i in range((digit - 1) * 3, digit * 3+x):
        if digit == 8 or digit == 9:
            ch = chr(ord('^') + i+1)
        else:
            ch = chr(ord('^') + i)
        ans += letterCombo(digits,curr + ch,idx+1)
    return ans

def letterComboCount(digits,curr='',idx=0):
    if idx == len(digits):
        return 1
    count = 0
    digit = int(digits[idx])
    x = 0 if digit < 7 or digit == 8 else 1
    for i in range((digit - 1) * 3, digit * 3 + x):
        if digit == 8 or digit == 9:
            ch = chr(ord('^') + i + 1)
        else:
            ch = chr(ord('^') + i)
        count += letterComboCount(digits,curr + ch,idx+1)
    return count

if __name__ == "__main__":
    print(letterCombo("2"))
    print(letterComboCount("2"))
