class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        if m == 0:
            return True
        n = len(matrix[0])
        
        # Check from first row
        for j in range(n):
            val = matrix[0][j]
            i = 1
            k = j + 1
            while i < m and k < n:
                if matrix[i][k] != val:
                    return False
                i += 1
                k += 1
        
        # Check from first column doesn't include the first element
        for i in range(1, m):
            val = matrix[i][0]
            j = 1
            k = i + 1
            while k < m and j < n:
                if matrix[k][j] != val:
                    return False
                k += 1
                j += 1
                
        return True