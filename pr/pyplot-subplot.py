# subplot(nrows, ncols, index)

import matplotlib.pyplot as plt
from math import log, log10

xs  = list(range(1, 101))
y1s = list(map(log, xs))
y2s = list(map(log10, xs))

plt.subplot(1, 2, 1)
plt.xlabel("x")
plt.ylabel("ln(x)")
plt.plot(xs, y1s, color='r')

plt.subplot(1, 2, 2)
plt.xlabel("x")
plt.ylabel("log10(x)")
plt.plot(xs, y2s, color='b')

plt.show()
