def tips(func):
    def nei(a, b):
        print('start')
        func(a, b)
        print('stop')
    return nei


@tips
def add(a, b):
    print(a+b)


print(add(6, 9))
