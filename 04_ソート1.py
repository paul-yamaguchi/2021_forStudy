def sort(A):
    for i in range(1,len(A)):
        insert(A, i)

def insert(A, i):
    temp = A[i]
    for j in range(i - 1, -1, -1): #最後から処理する時は-1,-1を活用
        if temp < A[j]:
            A[j + 1] = A[j]
        else:
            A[j + 1] = temp
            break
    else:
        A[0] = temp


lists = [6,3,8,5,7]
sort(lists)
print(lists) #sort~自体は動作なのでprint(sort~)しても何も出力されない

