def double(x):
    return 2*x

def square(x):
    return x**2;

def negative(x):
    return -x

def div2(x):
    return x/2

def generate_values(function, arguments):
    answer = []
    for i in arguments:
        answer.append(function(i))

    return answer

x_table = list(range(11))
 
print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))


