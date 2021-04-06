def sort(A):
    for i in range(0, len(A) - 1):
        if modify_order(A, i) == 0:
            break

def modify_order(A, i):
    exchange = 0
    for j in range(len(A) - 1, i, -1):
        if A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            exchange = exchange + 1
    return exchange

sort([9,2,7,4,5])

