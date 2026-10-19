class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in range(len(matrix)):
            L = 0
            R = len(matrix[row]) - 1

            while L <= R:
                mid = (L + R) // 2

                if matrix[row][mid] < target:
                    L = mid + 1
                elif matrix[row][mid] > target:
                    R = mid - 1
                else:
                    return True
        
        return False