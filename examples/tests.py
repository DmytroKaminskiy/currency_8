def add(x, y):
    return x + y


# # 1
# assert add(3, 6) == 9
# assert add(3, 7) == 10
# assert add(1, 2) == 3
#
# # 2
# assert add(3, 6) == 9
# assert add(3, -7) == -4
# assert add(0, 2) == 2

'''
1. Manual testing (Manual QA / Coder)
2. Auto Testing (automation QA / Coder)
3. Unittest (Coder) <--!!! (unittest/!pytest!)
4. Integration (???)
5. Load Testing (Coder)

func Code
unittests
Docs
'''

import pytest


@pytest.mark.parametrize(
    ['x', 'y', 'expected'],
    (
            (3, 7, 10),
            (3, -7, -4),
            (-2, 0, -2),
            (0, 0, 0),
    )
)
def test_add(x, y, expected):
    assert add(x, y) == expected



#
# import requests
#
# res = requests.get('http://localhost:8000/')
