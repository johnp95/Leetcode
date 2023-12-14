def fact(n):

    memo = {}
    def helper():
        if n in memo: return memo[n]
        if n == 1:
            return n

        memo[n] =  n * fact(n-1)
        return memo[n]

    return helper()
def combinations(elements):
    if len(elements) == 0: return [[]]

    firstEl = elements[0] 
    rest = elements[1:]

    combsWithoutFirst = combinations(rest) # => [[]]
    combsWithFirst = []

    for comb in combsWithoutFirst:
        combWithFirst = comb + [firstEl] 
        combsWithFirst += [combWithFirst]

    return combsWithoutFirst + combsWithFirst
def permutations(elements):
    if len(elements)==0: return [[]]
    firstEl = elements[0]
    rest = elements[1:]

    allPermutations = []
    permsWithoutFirst = permutations(rest) # => [[]]
    for perm in permsWithoutFirst:
        for i in range(len(perm) + 1):
            permWithFirst = perm[0:i] + [firstEl] + perm[i:]
            allPermutations += [permWithFirst]
    return allPermutations
def _sum1(nums):
    if len(nums)==0:return 0

    return nums[0] + _sum1(nums[1:])
def _sum2(nums):
    def helper(idx):
        if idx == len(nums): return 0
        

        return nums[idx] + helper(idx+1)

    return helper(0)
def fib(n):
    if n <= 2: return 1

    return fib(n-1) + fib(n-2)




if __name__ == '__main__':
    # print( fact(50))
    # print( combinations(['a','b','c']))
    # print(permutations(['a','b','c']))
    # print(_sum2([1,5,7,-2]))
    print(fib(7))