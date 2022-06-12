

class BaseTokenizer:
    def __init__(self, token):
        self.token = token

    def __iter__(self):
        yield from self.token.split("-")

class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())

class Tokenizer(UpperIterableMixin, BaseTokenizer):
    """
    >>> tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    >>> list(tk)
    ['28A2320B', 'FD3F', '4627', '9792', 'A2B38E3C46B0']
    """
    pass

if __name__ == "__main__":
    tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    print(list(tk))

"""
class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class Button(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size_x, size_y):
        super().__init__(pos_x, pos_y, size_x, size_y)
        self.status = False

    def toggle(self):
        self.status = not self.status


class LimitSizeMixin:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        size_x = min(size_x, 500)
        size_y = min(size_y, 400)
        super().__init__(pos_x, pos_y, size_x, size_y)


class LimitSizeButton(LimitSizeMixin, Button):
    pass

b = LimitSizeButton(10, 20, 2000, 1000)
print(b.size_x)
print(b.size_y)
"""