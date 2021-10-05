import random

print('猜數字遊戲')
x = random.randint(1, 50)
<<<<<<< HEAD
# print(x)

=======
#print(x)
>>>>>>> f3ddff10c3f45303ecaee0b0bc1d27dea028f59e
for i in range(5):
    bingo = False
    while True:
        try:
            y = int(input(f'第{i+1}/{5}次 請猜數字(1~50):'))
            if x == y:
                print('猜對了!')
                bingo = True
                break

            if x > y:
                print('猜高一點~')
            else:
                print('猜低一點~')

            break
        except:
            print('請輸入數字')

    if bingo:
        break
        
if bingo:
    print('恭喜過關!')
else:
    print(f'答案為{x}')
