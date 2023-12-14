from collections import defaultdict
#approach 1
def containsDuplicate1(nums):
    d = defaultdict(int)
    # O(n) Time, 0(n) Space
    for n in nums:
        d[n] += 1
        if d[n] > 1:
            return True
    return False
# approach 2
def containsDuplicate2(nums):
    if len(set(nums)) == len(nums) : return False
    return True

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(containsDuplicate1(nums))
    print(containsDuplicate2(nums))