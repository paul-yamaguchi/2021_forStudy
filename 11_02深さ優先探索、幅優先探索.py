from collections import deque

def depth_first_search(T): #深さ優先=スタック
    D = deque()
    if len(T) > 0:
        D.append(T)
    while len(D) > 0:
        L, a, R = D.pop()
        print(a, end=",")
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
    print()

def branch_first_search(T): #幅優先=キュー
    D = deque()
    if len(T) > 0:
        D.append(T)
    while len(D) > 0:
        L, a, R = D.popleft()
        print(a, end=",")
    if len(L) > 0:
        D.append(L)
    if len(R) > 0:
        D.append(R)
    print()

# def show(D): ステップを表示したい時使う
#     print("[", end=" ")
#     for (L, a, R) in D:
#         print(a, end="<-")
#         print("]")