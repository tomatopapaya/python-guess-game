import random

x = random.randint(1, 50)
print(x)

for i in range(5):
    y = int(input('請猜數字(1~50)'))
    if x == y:
        print('猜對了!')
        break

    print('猜錯了@@~')
