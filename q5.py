import matplotlib.pyplot as plt
import numpy as np

x = [0, 0.15, 0.31, 0.5, 0.6, 0.75]
y = [1, 1.004, 1.031, 1.117, 1.223, 1.422]

plt.ylabel('y numbers')
plt.xlabel('x numbers')

mymodel_1 = np.poly1d(np.polyfit(x, y, 1))
mymodel_2 = np.poly1d(np.polyfit(x, y, 2))
mymodel_3 = np.poly1d(np.polyfit(x, y, 3))
print("estimated polynomial for degree 1: ", mymodel_1)
print("estimated polynomial for degree 2: ", mymodel_2)
print("estimated polynomial for degree 3: ", mymodel_3)

t = np.linspace(-1, 1, 10000)
y0 = 1.147*(t**2) - 0.3257*t + 1.0111
y1 = 1.021*(t**3) - 0.01151*(t**2) - 0.001541*t + 1.0111
y2 = 0.5281*t + 0.9295

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(t, y0, 'r')
plt.plot(t, y1, 'g')
plt.plot(t, y2, 'b')


plt.scatter(x, y)
plt.show()
