class Solution:
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i][j - 1] and matrix[i - 1][j - 1]:
                    k = min(matrix[i - 1][j], matrix[i][j - 1])
                    matrix[i][j] = k + 1 if matrix[i - k][j - k] else k
                    if(matrix[i][j]!=k+1):
                        print(matrix[i][j])
                    else:
                        print("hey")
                        print(matrix[i][j])

        return sum(sum(row) for row in matrix)
        # count = 0;
        # n = len(matrix)
        # m= len(matrix[0])
        # sub = [[0]*(m+1) for _ in range(n+1)]
        # for row in range(1,n+1):
        #     for col in range(1,m+1):
        #         if(matrix[row-1][col-1]==1):
        #             sub[row][col]=1+min(sub[row][col-1],sub[row-1][col],sub[row-1][col-1])
        #             count+=sub[row][col]
        # return count

s=Solution()
print(s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))

# for i in range(n):
#     ans += matrix[n - 1][i]
# for j in range(m):
#     ans += matrix[i][m - 1];
# ans -= matrix[n - 1][m - 1]
# for i in range(n - 2, 0, -1):
#     for j in range(m - 2, 0, -1):
#         if (matrix[i][j] == 1):
#             matrix[i][j] = 1 + min(matrix[i + 1][j + 1], matrix[i][j + 1], matrix[i + 1][j])
#         else:
#             matrix[i][j] = 0
#     ans += matrix[i][j];
# return ans
