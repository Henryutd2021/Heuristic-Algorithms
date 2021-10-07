import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d

bounds = [0, 500]


def my_function(x):
    return (400 - np.square(x - 21)) * np.sin(x * np.pi / 6)


def optimize(bounds, maxIter, f, initVal=np.random.randint(bounds[1])):
    best_f = np.inf
    current_x = initVal
    try:
        step_range = int(input('Please enter an positive integer as maximum range of random steps or hit the ENTER to '
                               'use 10 as step: '))
    except ValueError:
        step_range = 10
    space_x = []
    space_y = []

    for i in range(maxIter):
        new_f = f(current_x)
        space_x.append(current_x)
        space_y.append(new_f)
        if new_f < best_f:
            best_f = new_f
            best_x = current_x
        step = np.random.randint(-step_range, step_range)
        current_x = np.clip(current_x + step, bounds[0], bounds[1])

    plt.figure().gca(projection="3d").scatter(range(maxIter), space_x, space_y, cmap="GnBu")
    plt.title('Random Walk')
    plt.show()
    plt.plot(range(bounds[1]), list(map(my_function, range(bounds[1]))))
    plt.title('cost function')
    plt.show()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(range(maxIter), space_x, 'deepskyblue', label='S')
    ax2 = ax1.twinx()
    ax2.plot(range(maxIter), space_y, 'coral', label='cost')
    ax1.set_xlabel('iterations')
    ax1.set_ylabel('random S')
    ax2.set_ylabel('cost')
    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)
    plt.show()
    print('After %d iteration,the best_s is' % maxIter, best_x, 'and the minimum cost is', best_f)


if __name__ == '__main__':
    try:
        initVal = int(input('Please enter an initial s or hit the ENTER to use a randam value:'))
    except ValueError:
        try:
            maxIter = int(input('Now a random value for s is adopted, please enter the maximum number of iterations:'))
        except ValueError:
            print("Since you don’t want to enter anything, the operation is over!")
        else:
            optimize(bounds, maxIter, my_function)
    else:
        try:
            maxIter = int(input('Please enter the maximum number of iterations:'))
            optimize(bounds, maxIter, my_function, initVal)
        except ValueError:
            print("Since there is no iterations, the operation is over!")
