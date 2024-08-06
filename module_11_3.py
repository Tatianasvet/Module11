import inspect


class SomeClass:

    some_attr_1 = 4

    def __init__(self):
        self.some_attr_2 = 'sting'
        self.some_attr_3 = 3.14159
        self.some_attr_4 = ['l', 'i', 's', 't']
        self.some_attr_5 = {'d': 4, 'i': 9, 'c': 3, 't': 16}
        self.some_attr_6 = (2, 'ple')
        self.some_attr_7 = True
        self.some_attr_8 = None

    def some_method(self):
        pass


def introspection_info(obj):
    res = {'type': type(obj).__name__, 'attributes': [], 'methods': [], 'module': None}

    for name in dir(obj):
        if callable(getattr(obj, name)):
            res['methods'].append(name)
        else:
            res['attributes'].append(name)

    module = inspect.getmodule(obj)
    if hasattr(module, '__name__'):
        res['module'] = module.__name__

    if hasattr(obj, '__iter__'):
        res['len'] = len(obj)

    return res


o = SomeClass()
info_1 = introspection_info(42)
info_2 = introspection_info(o)
print(info_1)
print(info_2)
