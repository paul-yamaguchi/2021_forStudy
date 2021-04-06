#単独では動作しない。目的に応じて関数leaf,evaluation,edgeを定義する。

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

