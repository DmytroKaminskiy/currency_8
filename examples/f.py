

d = {
    'f1': {
        'a': 1,
        'b': 3,
        'op': 'plus',
        'koef': 1.1,
    },
}

def plus(a, b, koef):
    return (a + b) * koef

def diff(a, b):
    return a - b


mapper = {
    'plus': plus,
    'diff': diff,
}

def parse(params):
    for f_name, f_params in params.items():
        print(f_name)
        print(f_params)
        operation_name = f_params.pop('op')
        func = mapper[operation_name]
        result = func(**f_params)
        print(result)



parse(d)
