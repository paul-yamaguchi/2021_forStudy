def max(A, n):
    def f(t): return t[1]/t[2] #重量当たりの価値を返す関数f
    A.sort(key=f, reverse=True) #sortはAを整列して上書きする
    b = 0; items =[]
    for (i, p, w) in A:
        if n >= w:
            b = b + p
            items = items + [(i, w)]
            n = n - w #荷物1個入れたら価値を増やして残り重量を減らす
        else:
            b = b + p * n / w #今回は荷物を分割できるので残り重量を分割して詰める
            items = items + [(i, n)]
            break
    return (b, items)

lists = [("A",400,5),("B",300,4),("C",200,2),("D",300,1)]
print(max(lists, 5))
#(660.0, [('D', 1), ('C', 2), ('A', 2)])
