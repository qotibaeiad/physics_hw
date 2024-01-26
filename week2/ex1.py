import numpy as np

qn = int(input())

if qn == 1:
    result = np.arange(0.0, 10.0, 1.0)
    print([round(num, 5) for num in result])
elif qn == 2:
    result = np.power(10.0, np.arange(10.0))-1.0
    print(result)
elif qn == 3:
    b = np.power(10.0, np.arange(10.0))-1.0
    c = np.diff(b)
    print(c)
elif qn==4:
    b = np.power(10.0, np.arange(10.0))-1.0
    c = np.diff(b)
    d=np.flip(c)
    print(d)
elif qn==5:
    b = np.power(10.0, np.arange(10.0))-1.0
    c = np.diff(b)
    d=np.flip(c)
    e=np.cumsum(d)
    print(e)
elif qn==6:
    x=np.arange(0.0,6.28,0.01)
    y = np.power(np.sin(x),2.0)
    print(y[:10])
elif qn==7:
    a, b, d = 0, 6.28, 0.01
    x = np.arange(a, b, d)
    sum = np.sum(np.power(np.sin(x),2.0) * d)
    print(sum)
elif qn==8:
    x=np.arange(0.0,6.28,0.01)
    y = np.power(np.sin(x),2.0)