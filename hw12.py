import math
import time

formulas_list = ["abs(x**3 - x**0.5)", "abs(math.sin(x) * x**2)"]


argument_list = []
for i in range(10000):
    argument_list.append(i/10)

print(argument_list)

for formula in formulas_list:
    result_list = []
    print(formula)
    start=time.time()
    for x in argument_list:
        result_list.append(eval(formula))
    stop=time.time()
    print('eval time:',stop-start)


for formula in formulas_list:
    result_list = []
    print(formula)
    start=time.time()
    compiled_formula=compile(formula,'test', 'eval')
    for x in argument_list:
        result_list.append(eval(compiled_formula))
    stop=time.time()
    print('compile time:',stop-start)