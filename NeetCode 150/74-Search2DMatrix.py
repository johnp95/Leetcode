class Solution:
    def searchMatrix(self, matrix,target):

        rows, cols = len(matrix),len(matrix[0])

        for i in range(rows):

            l,r = 0, cols-1

            while l <= r:   

                mid = (l+r)//2
                if matrix[i][mid] < target:
                    l = mid + 1
                elif matrix[i][mid] > target:
                    r = mid - 1
                else:
                    return True
        return False
        
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Solution().searchMatrix(matrix,3))