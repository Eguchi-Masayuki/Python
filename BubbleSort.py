import random
def bubbleSort(array):#昇順にソートする関数
    long=len(array)-1
    for n in range(long):
        for i in range(long-n):
            if(array[i]>array[i+1]):#array[i]がarray[i+1]より大きければ交換を行う
                t=array[i+1]
                array[i+1]=array[i]
                array[i]=t
    return array
rand=[]#ランダムな数値を格納するリスト
for i in range(100):#要素数100のリストを作成
    ran=random.randint(-100,100)#-100から100までのランダムな数値を生成
    rand.append(int(ran))#リストに数値を格納
print("ソート前のリスト:"+str(rand))
print("昇順にソート後のリスト:"+str(bubbleSort(rand)))