
def sum(a, b):
    return a+b

def multi(a, b):
    return a*b

def divid(a, b):
    return a/b


actiion_map = {
    'test':sum,
    'test2':multi,
    'test3':divid
}

if __name__=='__main__':
    result=actiion_map.get('test111111', divid)
    print(result(1,3))
