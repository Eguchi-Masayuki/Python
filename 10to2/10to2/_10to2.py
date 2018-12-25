#二進数に変換
def cardConvR(x):
    a=[]
    while x!=0:
        a.append(int(x%2))
        x=x//2
    return a

def main():
    print("10進数を基底変換します。")
    print("変換する非負の整数:",end="")
    try:
        num=int(input()) 
        if num<0:
            print("正の整数を入力してください。\n")
            main()
        else:
            print("2進数では",end="")
            #リストを逆順にソート
            ans=cardConvR(num)[::-1]
            for i in ans:
                print(i,end="")
            print("です。")

    #例外処理
    except:
        print("非負の整数を入力してください。\n")
        main()

#実行部分
main()