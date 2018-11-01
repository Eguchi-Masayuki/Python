def main():
    print("10進数を基底変換します。")
    print("変換する非負の整数:",end="")
    try:
        num=int(input()) 
        if num<0:
            print("正の整数を入力してください。\n")
            main()
        else:
            print("何進数に変換しますか(2-36):",end="")
            log=int(input())
            if log<2 or log>36:
                print("2以上36以下の数を入力してください。\n")
                main()
            else:
                ##リストを逆順にソート
                ans=cardConvR(num,log)[::-1]
                for i in ans:
                    print(i,end="")
                print("です。")
                Retry()

    ##例外処理
    except:
        print("非負の整数を入力してください。\n")
        main()

##n進数に変換
def cardConvR(x,r):
    dchar="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a=[]
    while x!=0:
        a.append(dchar[int(x%r)])
        x=x//r
    return a

##繰り返し確認
def Retry():
    print("もう一度しますか(1…はい/0…いいえ):",end="")
    try:
        retry=int(input())
        if retry==0 or retry==1:
            if retry==1:
                print()
                main()
        else:
            print("0または1を入力してください。") 
            Retry()

    ##例外処理
    except:
        print("0または1を入力してください。")
        Retry()

##実行部分
main()