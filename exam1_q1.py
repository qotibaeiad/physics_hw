import numpy as np


"""
#quiestion 1
def max_div(a,b):
    max_num=max(a,b)
    for i in range(max_num,0,-1):
        if(a%i==0 and b%i==0):
            print(i)
            return 
    print(0)
    return 0


#question 2
def series(a,b,d):
    sum=0
    series=[]
    for i in range(a,b+1,d):
        series.append(i)
        sum+=i
    print(series)
    print(sum)

a = float(input("start: "))
b = float(input("stop: "))
d = float(input("step: "))
#series(a,b,d)

"""
def input_vector():
    vector_str = input("Enter vector components separated by commas (e.g., 1,2,3): ")
    vector_components = [float(x) for x in vector_str.split(',')]
    radian_degree = np.arctan(vector_components[1]/vector_components[0])
    return np.degrees(radian_degree)

vector = input_vector()

print("Vector:", vector)
