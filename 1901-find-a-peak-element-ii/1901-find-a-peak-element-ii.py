class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            max_row = 0
            for r in range(rows):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r
            left_val = mat[max_row][mid - 1] if mid > 0 else -1
            right_val = mat[max_row][mid + 1] if mid < cols - 1 else -1
            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row, mid]
            elif left_val > mat[max_row][mid]:
                right = mid - 1
            else:
                left = mid + 1