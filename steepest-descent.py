import numpy as np
import matplotlib.pyplot as plt
import scipy.misc


def f(x):
    return (np.power(x, 2) / 10) - 2 * np.sin(x)


def df(x):
    return (x / 5) - 2 * np.cos(x)


def ddf(x):
    return 2 * np.sin(x) + 1/5


def newtons_method():
    xk = -6
    xpoints = []
    ypoints = []

    for i in range(1000):
        xk1 = xk - df(xk) / ddf(xk)

        if abs(xk - xk1) <= 1e-4:
            break
        xpoints.append(xk)
        ypoints.append(f(xk))
        xk = xk1

    print(xk, i)
    plot_fn(xpoints, ypoints)


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

    alphas = []
    for i in range(len(x)):
        alpha = 1 - i / len(x)
        alphas.append(alpha)

    if x is not None:
        ax.plot(x_points, y_points, 'go')

    plt.plot(x, fn)
    plt.show()


def grad_descent():
    alpha = 1
    xk = 0.5
    xk1 = xk
    gamma = 1

    xpoints = []
    ypoints = []
    for i in range(1000):
        dk = -1 * df(xk)

        if abs(dk) <= 1e-4:
            break

        xk1 += alpha * dk
        alpha = 1 - i / 20
        xpoints.append(xk)
        ypoints.append(f(xk))
        xk = xk1

    print(xk, i)
    plot_fn(xpoints, ypoints)


# grad_descent()
newtons_method()
