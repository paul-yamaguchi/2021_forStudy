from collections import deque
#deque : double-ended que(両端キュー)

D = deque() #空のキュー[]を作成
D.append("A")
D.append("B")
D.append("C")

D.pop() #C:右端から削除された要素
D.popleft() #A:左端から削除された要素
print(D) #deque("B")
