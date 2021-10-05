import random

print('猜數字遊戲')
start = int(input('start:'))
end = int(input('end:'))
count = int(input('count:'))
low = start
high = end

x = random.randint(start, end)
# print(x)
for i in range(count):
    bingo = False
    while True:
        try:
            print(f'{low}~{high}')
            y = int(input(f'第{i+1}/{count}次 請猜數字({start}~{end}):'))
            if x == y:
                print('猜對了!')
                bingo = True
                break

            if x > y:
                print('猜高一點~')
                low = y+1 if y > low else low
            else:
                print('猜低一點~')
                high = y-1 if y < high else high
            break
        except:
            print('請輸入數字')

    if bingo:
        break

if bingo:
    print('恭喜過關!')
else:
    print(f'答案為{x}')
