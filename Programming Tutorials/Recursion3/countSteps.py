# def numberOfSteps(num):
#     if num < 1 : return 0
#     if num % 2 == 0 : 
#         num /=2
#     else:
#         num -= 1
#     return 1 + numberOfSteps(num)
def numberOfSteps(num,steps=0):
    if num < 1 : return steps
    if num % 2 == 0 : 
        return numberOfSteps(num//2,steps+1)
    return numberOfSteps(num-1,steps+1)
    
if __name__ == '__main__':
    print(numberOfSteps(14))