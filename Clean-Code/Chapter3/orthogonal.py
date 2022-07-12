"""Clean Code in Python - Chapter 3: General traits of good code
> Orthogonality
"""


def calculate_price(base_price: float, tax: float, discount: float) -> float:
    """
    >>> calculate_price(10, 0.2, 0.5)
    6.0
    >>> calculate_price(10, 0.2, 0)
    12.0
    """
    return (base_price * (1 + tax)) * (1 - discount)


def show_price(price: float) -> str:
    """
    >>> show_price(1000)
    '$ 1,000.00'
    >>> show_price(1_250.75)
    '$ 1,250.75'
    """
    return "$ {0:,.2f}".format(price)


def str_final_price(base_price: float, tax: float, discount: float, fmt_function=str) -> str:
    """
    fmt_function에 인자를 기본으로 str로 두어 calculate_price의 함수 호출 결과를 str로 사용하거나,
    함수를 넣어서 결과를 바꿀 수 있도록 한다.
    """
    return fmt_function(calculate_price(base_price, tax, discount))


if __name__ == "__main__":
    print(str_final_price(1000, 0.2, 0.1))
    """
    >>> str_final_price(10, 0.2, 0.5)
    '6.0'
    >>> str_final_price(1000, 0.2, 0)
    '1200.0'
    """
    print(str_final_price(1000, 0.2, 0.1, fmt_function=show_price))
    """
    >>> str_final_price(1000, 0.2, 0.1, fmt_function=show_price)
    '$ 1,080.00'
    """
