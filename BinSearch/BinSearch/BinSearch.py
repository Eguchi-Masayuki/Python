import random
def bubbleSort(array):#昇順にバブルソートを行う関数
    long=len(array)-1
    for n in range(long):
        for i in range(long-n):
            if(array[i]>array[i+1]):
                t=array[i+1]
                array[i+1]=array[i]
                array[i]=t
    return array

def binSearch(array,length,key):#二分探索を行う関数
    pl=0
    pr=length
    while pl<=pr:
        pc=(pl+pr)//2#中央のインデックス
        if array[pc]==key:#キー値と中央値が一致した
            return pc
        elif array[pc]>key:#中央値がキー値より大きいので前半に絞る
            pr=pc-1
        else:
            pl=pc+1#中央値がキー値より小さいので前半に絞る
    return -1#探索失敗

rand=[]
for i in range(100):
    n=random.randint(-100,100)
    rand.append(n)
print("ソート前のリスト:"+str(rand))
rand=bubbleSort(rand)
print("昇順にソート後のリスト:"+str(rand))
leng=len(rand)-1
print("探す値:",end="")
try:
    key=int(input())
except:
    print("整数を入力してください。")
else:
    ans=binSearch(rand,leng,key)
    if ans!=-1:
        print(str(key)+"はリストのインデックス"+str(ans)+"番目にあります。")
    else:
        print(str(key)+"はリスト内に存在しません。")
