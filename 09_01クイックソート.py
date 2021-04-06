def sort(A):
    if len(A) < 2:
        return A
    p = A[0]
    X, Y = divide(p, A[1:])
    return sort(X) + [p] + sort(Y)

#ピボットpとリストAを受取り、pを境に左右に振り分けリストのタプルを返す
def divide(p, A): 
    if len(A) < 1:
        return([], [])
    X, Y = divide(p, A[1:])
    a = A[0]
    if a < p:
        return ([a] + X, Y)
    else:
        return (X, [a] + Y) 

a = divide(10, [3,20,1,30,2])
print(a) #([3, 1, 2], [20, 30]) divideは10をピボットに左右に分ける
b = sort([3,20,1,30,2])
print(b) #[1, 2, 3, 20, 30]