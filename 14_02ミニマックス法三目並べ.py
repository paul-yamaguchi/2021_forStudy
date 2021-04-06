def leaf(n): #盤面nで勝敗が決まっているか判定する
    return((triple(n, "0") and not triple(n, "X")) or (not triple(n, "0") and triple(n, "X") or ("_" not in n[0] + n[1] + n[2])))

def triple(n, p): #盤面nの中でpが縦横斜めに一列に揃っているかどうかを判定
    for (a,b,c) in [(0,0,0), (1,1,1),(2,2,2),(0,1,2)]:
        if(n[a][0] == n[b][1] == n[c][2] == p or n[2][a] == n[1][b] == n[0][c] ==p):
            return True
    return False

def evaluation(n): #〇が揃ったら100(勝)、×は0(負)、引き分けは50を返す
    if triple(n, "0"):
        return 100
    elif triple(n, "X"):
        return 0
    else:
        return 50

def edge(n): #取りうる手を全通り列挙し、次の盤面のリストを返す
    L = n[0] + n[1] + n[2]
    Ns = []
    player = "0"
    if L.count("0") > L.count("X"):
        player = "X"
    for i in range(len(L)):
        if L[i] == "_":
            L2 = L[:]
            L2[i] = player
            Ns = Ns + [L2]
    return [[[a,b,c], [d,e,f], [g,h,i]] for (a,b,c,d,e,f,g,h,i) in Ns]

#14_01のコピー
def my_turn(n):
    if leaf(n):
        return evaluation(n)
    max = 0
    for next in edge(n):
        temp = your_turn(next)
        if temp > max:
            max = temp
    return max

def your_turn(n):
    if leaf(n):
        return evaluation(n)
    min = 100
    for next in edge(n):
        temp = my_turn(next)
    if temp < min:
        min = temp
    return min


n = [["0", "_", "_"],["0", "X", "_"], ["X", "0", "X"]]
print(my_turn(n))
