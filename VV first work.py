import random
from math import fabs
yy = 0
numbers = []
otr=[]
for i in range(17):
    number1 = random.randint(-50, 50)
    numbers.append(number1)
print(numbers)
print("Сумма =",sum(numbers))
for g in numbers:
    if g < 0:
        otr.append(g)
otr.append("END")
ggr = otr.index("END")
otr.remove ("END")
print("Сумма отрицательных чисел",sum(otr))
tt = sum(otr)
h=abs(tt)
print(h)
jj = h//ggr
print(jj,"Среднее")
for plus in numbers:
    if jj<plus:
        yy += plus
print(yy)