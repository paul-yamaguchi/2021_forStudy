def show(T): #余分な()を除去して表示
    if len(T) == 0:
        return ''
    L, data, R = T
    return "(" + show(L) + str(data) + show(R) + ")"

def remove(T, n):
    if len(T) == 0:
        return ()
    L, data, R = T
    if n == data:
        if len(L) == 0:
            return R
        if len(R) == 0:
            return L
        m, X = remove_min(R)
        return (L, m, X) #()で括ってあるのはタプル
    if n < data:
        return (remove(L, n), data, R)
    return (L, data, remove(R, n))

def remove_min(T):
    L, data, R = T
    if len(T) == 0:
        return (data, R)
    m, X = remove_min(L)
    return (m, (X, data, R))
