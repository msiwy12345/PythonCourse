import math

argument_list=[]
x=0
for i in range(100):
    argument_list.append(x)
    x=x+0.1


print(argument_list)


formula = input('enter a formula: ')
for x in argument_list:
    print(eval(formula))

