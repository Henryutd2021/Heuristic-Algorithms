import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from scipy import integrate


class SimAnneal(object):
    def __init__(self, T, M, interval, cst=15000):
        self.T = T
        self.M = M
        self.interval = interval
        self.cst = cst

    def clip(self, x):
        a, b = self.interval
        return max(min(x, b), a)

    def random_start(self):
        a, b = self.interval
        return [round(a + (b - a) * rn.random_sample()), round(a + (b - a) * rn.random_sample())]

    def cost_function(self, x):
        #s1, s2 = x
        return
        # return 10 ** 9 - (625 - np.square(s1 - 25)) * (1600 - np.square(s2 - 10)) * np.sin(s1 * np.pi / 10) * np.sin(
        #     s2 * np.pi / 10)

    def acceptance_probability(self, cost, new_cost, temperature):
        return np.exp(- (new_cost - cost) / (self.cst*temperature))

    def temperature(self, fraction):
        return max(0.01, min(1, 1 - fraction))

    def random_neighbour(self, x):
        delta1 = rn.randint(-25, 25)
        delta2 = rn.randint(-25, 25)
        x1, x2 = x
        return [round(self.clip(x1 + delta1)), round(self.clip(x2 + delta2))]

    def annealing(self, random_start,
                  cost_function,
                  random_neighbour,
                  acceptance,
                  temperature,
                  maxsteps=1000,
                  debug=True):
        T = self.T
        M = self.M
        state = self.random_start()
        cost = self.cost_function(state)
        states, costs = [state], [cost]
        state = [i+1 for i in state]
        for step in range(1, maxsteps):
            if T > 1e-9:
                fraction = step / float(maxsteps)
                new_cost = self.cost_function(state)
                if debug:
                    print("Step #{0}/{1} : T = {2:.1f}, state = {3}, cost = {4},"
                          " new_cost = {5} ...".format(step, maxsteps, T, state, cost, new_cost))
                if new_cost < cost:
                    states.append(state)
                    costs.append(new_cost)
                    state = [i+1 for i in state]
                    cost = new_cost
                elif self.acceptance_probability(cost, new_cost, T) > rn.random():
                    print("  ==> Accept it!")
                    state = [i + 1 for i in state]
                    new_cost = cost_function(state)
                    if new_cost < cost:
                        state = [i + 1 for i in state]
                        cost = new_cost
                    else:
                        state = self.random_neighbour(state)
                else:
                    print("  ==> Reject it...")
                    state = self.random_neighbour(state)
                while M <= 0:
                    T = T * self.temperature(fraction)
                    M = 5
                M -= 1
            else:
                print('after %d steps searching because of T < 1e-9, Search stopped' % step)
                break
        return state, self.cost_function(state), states, costs

    def display(self, states, costs):
        sns.set(context="talk", style="darkgrid", palette="hls", font="sans-serif", font_scale=1.05)
        FIGSIZE = (19, 10)
        mpl.rcParams['figure.figsize'] = FIGSIZE
        plt.figure()
        plt.suptitle("Evolution of states and costs of the simulated annealing")
        plt.subplot(121)
        plt.plot(np.array(states).reshape(-1, 1)[::2], 'r')
        plt.plot(np.array(states).reshape(-1, 1)[1::2], 'g')
        plt.title("States")
        plt.subplot(122)
        plt.plot(costs, 'b')
        plt.title("Costs")
        plt.show()
        fig = plt.figure()
        ax = Axes3D(fig)
        x = range(states[-1][0]-15, states[-1][0]+10)
        y = range(states[-1][1]-15, states[-1][1]+10)
        X, Y = np.meshgrid(x, y)
        Z = self.cost_function([X, Y])
        plt.xlabel('x')
        plt.ylabel('y')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='GnBu')
        plt.savefig('fig.png', bbox_inches='tight')
        ax.view_init(elev=60, azim=45)
        ax.scatter(states[-1][0], states[-1][1], costs[-1], c='r', marker='o')
        plt.show()


if __name__ == '__main__':
    sa = SimAnneal(T=1000, M=5, interval=(0, 127))
    state, c, states, costs = sa.annealing(sa.random_start, sa.cost_function, sa.random_neighbour, sa.acceptance_probability, sa.temperature,
                                        maxsteps=200, debug=True)

    print(states)
    print(costs)

    sa.display(states, costs)
































