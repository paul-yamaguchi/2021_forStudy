def sort(A):
    if len(A) < 2:
        return A
    c = len(A) // 2 #//は除算の整数部分
    return merge(sort(A[:c]), sort(A[c:])) #Aはそのままで新しいlistを返す

def merge(X, Y):
    if len(X) < 1:
        return Y
    if len(Y) < 1:
        return X
    if (X[0] > Y[0]):
        return [Y[0]] + merge(X, Y[1:])
    else:
        return [X[0]] + merge(X[1:], Y)

lists = [19,12,3,8,25,18,100,1]
sorted_list = sort(lists)
print(lists) #[19, 12, 3, 8, 25, 18, 100, 1]
print(sorted_list) #[1, 3, 8, 12, 18, 19, 25, 100]
