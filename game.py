print('GAME OF SNAKE,WATER AND GUN','2 PLAYER GAME OR PLAY WITH BOT')
print ('enter 1 for snake, 2 for water & 3 for gun')
import random
try:
    b=input('enter whether you want to play bot or your friend;')
    while True:
        if b.upper()=='BOT':
            a=int(input("enter player's choice;"))
            c=random.randint(1,3)
            print("BOT'S CHOICE:",c)
            if a==1 and c==2 or a==2 and c==3 or a==3 and c==1:
                print('user wins!')
            elif a==1 and c==3 or a==2 and c==1 or a==3 and c==2:
                print('bot wins!')
            elif a==1 and c==1 or a==2 and c==2 or a==3 and c==3:
                print('draw!')
            else:
                print('ERROR!!!')
        elif b.upper()=='FRIEND':
            d=int(input("enter player 1's choice;"))
            e=int(input("enter player 2's choice;"))
            if d==1 and e==2 or d==2 and e==3 or d==3 and e==1:
                print('user wins!')
            elif d==1 and e==3 or d==2 and e==1 or d==3 and e==2:
                print('bot wins!')
            elif d==1 and e==1 or d==2 and e==2 or d==3 and e==3:
                print('draw!')
            else:
                print('ERROR!!!')
        else:
            print('error!!!')
        ch=input('wanna go for another round (y/n):')
        if ch.upper()=='N':
            break
except:
    print('ERROR!!!.....KINDLY CHECK THE INPUT!!!')
finally:
          print('THE END!!!')
          print('HAVE A NICE DAY!!!')

            
            
        
    
