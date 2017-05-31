import matplotlib.pyplot as plt
from pylab import *

x = linspace(-5, 5, 10,)

func = x**3 + 2
y = func
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('func')
show()
