from Common import ConVar
import csv

def factorial_iteravice(n):
    result = 1
    for i in range(1, n+1):
        result *= (1-ConVar.qx_list[i])
    return result

def read_csv():
    f = open(ConVar.CSV_PATH, 'r',encoding='utf-8-sig')
    rea = csv.reader(f)
    qx_list = [i[1] for i in rea][1:]
    qx_list = list(map(float, qx_list))
    qx_list.insert(0,1)
    return qx_list