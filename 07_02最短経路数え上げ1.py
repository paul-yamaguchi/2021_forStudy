def counting(a, b, X): #a * b列の全て-1の格子を作る。Xは通れない座標のリスト
    A = [[-1 for j in range(b + 1)] for i in range(a + 1)]
    for i in range(a + 1):
        A[i][0] = 0
    for j in range(b + 1):
        A[0][j] = 0
    for (i, j) in X: #×印は通れないので0通りにする
        A[i][j] = 0
    A[1][1] = 1
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if A[i][j] == -1:
                A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[a][b]

print(counting(5,6,[(2,3),(4,5)])) #32
