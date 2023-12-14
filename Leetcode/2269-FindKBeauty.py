class Solution:
    def __init__(self):
        pass

    def findNumber(self,num,k):
        str_num = [str(i) for i in str(num)]
        start = 0
        lst = []
        kBeauty = 0
        for end in range(len(str_num)):
            lst += str_num[end]
            if end-start+1 == k:
                curr_num = ''.join(lst)
                if int(curr_num) != 0:
                    if num % int(curr_num) == 0:
                        kBeauty +=1
                lst.pop(0)
                start +=1

        return kBeauty
        
solution1 = Solution().findNumber(240,2)
print()
solution2 = Solution().findNumber(10,1)
print()
solution3 = Solution().findNumber(430043,2)
print()
solution4 = Solution().findNumber(30003,3)

print(solution1)
print(solution2)
print(solution3)
print(solution4)