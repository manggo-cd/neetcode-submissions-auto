class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        t, b = 0, ROW - 1
        while t <= b:
            mid = (t + b) // 2
            if target > matrix[mid][-1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                break

        if not (t <= b):
            return False

        row = (t + b) // 2
        l, r = 0, COL - 1

        while l <= r:
            col = (l + r) // 2

            if matrix[row][col] == target:
                return True

            if target > matrix[row][col]:
                l = col + 1

            else:
                r = col - 1
        
            
        return False
            


        