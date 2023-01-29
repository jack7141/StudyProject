import logging

test = {
    'trd_p': 123,
    'quantity': 123
}

def str_to_number(str_num: str, type_cls=float):
    try:
        str_num = str(str_num).replace(',', '')
        if not str_num:
            return 0

        if type_cls != float:
            str_num = float(str_num)
        return type_cls(str_num)
    except ValueError as e:
        logging.warning(f"ValueError:{str(e)}")
        return 0

def re(result):
    """
    if result < 0:
        return result
    else:
        return 22222
    """
    return result if result < 0 else 22222
if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    # trd_p가 True면 그냥 계산하고 아니면, 1 * x['quantity'] 이렇게 처리해라~
    result = lambda x: str_to_number(x['trd_p'], float) * str_to_number(x['quantity'], float) if x['trd_p'] else 1 * x['quantity']
    data = result(test)

    print(data)
    print(re(data))