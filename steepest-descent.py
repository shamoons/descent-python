import numpy as np
import matplotlib.pyplot as plt
import scipy.misc


def f(x):
    return (x**2 / 10) - 2 * np.sin(x)


def plot_fn(x_points=None, y_points=None):
    x = np.arange(-10, 10, 0.1)
    fn = f(x)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if x is not None:
        ax.plot(x_points, y_points, 'go')

    plt.plot(x, fn)
    plt.show()


xk = -5
xk1 = xk
alpha = 1
xpoints = []
ypoints = []
for i in range(1000):
    dk = -1 * scipy.misc.derivative(f, xk)
    xk1 += alpha * dk
    if xk1 - xk == 0:
        break
    xpoints.append(xk)
    ypoints.append(f(xk))
    xk = xk1
    print('x', xk)

print(xk, i)
plot_fn(xpoints, ypoints)
