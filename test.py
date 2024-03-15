
def reserve(x:int)->int:
    y = 0
    while 0 < x:
        y = y * 10 + x % 10
        x //= 10

    return y


print(f'123 {reserve(123)}')
print(f'1200 {reserve(1200)}')