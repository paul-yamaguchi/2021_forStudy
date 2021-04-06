def show(T): #余分な()を除去して表示
    if len(T) == 0:
        return ''
    L, data, R = T
    return "(" + show(L) + str(data) + show(R) + ")"

def insert(T,n): #insert(n)する度に挿入
    if len(T) == 0:
        return ((), nn ())
    L, data, R = T
    if n == data:
        return T
    if n < data:
        return (insert(L,n), data, R)
    return (L, data, insert(R, n))

def search(T, n): #T内にnがあるか探索、あればTrue
    if len(T) == 0:
        return False
    L, data, R = T
    if n ==data:
        return True
    if n < data:
        return search(L, n)
    return search(R, n)
