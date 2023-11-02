def double(x):
    return 2*x

def square(x):
    return x**2;

def negative(x):
    return -x

def div2(x):
    return x/2

number = 8
transformations = [double, square, negative, div2]
tmp_return_value = number

for i in transformations:
    tmp_return_value = i(tmp_return_value)
    print(tmp_return_value)