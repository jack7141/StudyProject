def fibo_deco(func):
    res = {}

    print('fibo_deco in')
    
    def inner(*args):
        n = args[0]
        if res.get(n):
            return res.get(n)
        r = func(n)
        res[n] = r
        return r

    return inner


@fibo_deco
def fibo(n):
    print('fibo in')
    if n < 3:
        return 1

    return fibo(n - 1) + fibo(n - 2)


print(fibo(10))