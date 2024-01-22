import numpy as np

qn = int(input())

if qn == 1:
    result = np.arange(0.0, 10.0, 1.0)
    print([round(num, 5) for num in result])
elif qn == 2:
    result = np.power(10.0, np.arange(10.0))-1.0
    print([round(num, 5) for num in result])
elif qn == 3:
    b = np.power(10.0, np.arange(10.0))-1.0
    c = np.diff(b)
    print([round(num, 5) for num in c])
