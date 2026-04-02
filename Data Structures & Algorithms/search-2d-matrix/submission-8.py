class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1


        while top <= bot:
            mid = (top + bot) // 2

            if target < matrix[mid][0]:
                bot = mid - 1

            elif target > matrix[mid][-1]:
                top = mid + 1

            else:
                break

        row = (top + bot) // 2
        l, r = 0, col - 1

        while l <= r:
            mid = (l + r) // 2
            
            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1

        return False