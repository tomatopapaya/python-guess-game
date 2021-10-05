import random

x = random.randint(1, 50)
print(x)

for i in range(5):
    y = int(input('請猜數字(1~50)'))
    if x == y:
        print('猜對了!')
        break

    if x > y:
        print('猜高一點~')
    else:
        print('猜低一點~')

print(f'答案為{x}')
