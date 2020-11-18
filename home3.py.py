import random
setNum=random.randint(0,20)
print("在1~20(包含1和20)之間猜一個數,可猜5次.")
for guessTaken in range(1,6):
    print("請猜數")    
    guessNum=int(input())
    if guessNum > 20 or  guessNum < 0:
        print("請輸入0以上,20以下的數")
    elif guessNum < setNum:
        print("大一點") 
    elif guessNum > setNum:
        print("小一點")
    else: break   
    if guessNum == setNum:
        print("恭喜你,第"+ str(guessTaken)+"次猜對了.")    
    else:
        print("很遺憾,你沒有猜到設定數:"+ str(setNum))
     
 











