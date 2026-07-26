class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        maxval=float('-inf')
        ans=[-1,-1]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]>maxval:
                    maxval=mat[i][j]
                    ans=[i,j]
        return ans