from collections import Counter

def containsDuplicate(nums):

        counter = Counter(nums)

        for v in counter.values():
            if v > 1:
                return True
        return False

test_cases = [[1,2,3,4],[1,1,2,3]]

for t in test_cases:
     print(containsDuplicate(t))

        