def sumOfNaturalNumbers(inputNumber):
    if inputNumber == 1 : return inputNumber
    return inputNumber + sumOfNaturalNumbers(inputNumber-1)

result = sumOfNaturalNumbers(5)    
print(result)
