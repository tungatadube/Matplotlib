import matplotlib.pyplot as plt
from pylab import *

x = linspace(-5, 5, 10,)

Vel = x**3 + 2
y = Vel
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('Vel')
show()