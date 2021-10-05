import random

x = random.randint(1, 50)
print(x)


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
