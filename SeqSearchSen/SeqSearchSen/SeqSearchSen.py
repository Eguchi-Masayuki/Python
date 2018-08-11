try:
    file = open('num_input.txt')#num_input.txtを開く
except:
    print("ファイルが見つかりません。")#ファイルが見つからないときの例外処理
else:
    line=[]
    line=file.readline().split(",")#カンマ区切りの数値をリストに代入する。
    file.close
    print("探索リスト:"+str(line))#リストの中身を表示
    long=len(line)
    print("要素数は"+str(long)+"です。")#リストの要素数を表示
    print("探す値:",end="")
    try:
        num=int(input())#キー値の指定
        line.append(str(num))#番兵をリストに追加
        #print(line) #新しいリスト
    except:
        print("整数を入力してください。")#数字以外が入力されたときの例外処理
    else:
        #print(len(line)) #新しいリストの要素数
        if line.index(str(num))==(len(line)-1):#リストの最後の要素にキー値があれば探索失敗
            print("探索失敗")
        else:
            print("探す値はリストの"+str(line.index(str(num))+1)+"番目にあります。")