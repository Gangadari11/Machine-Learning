import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08

    plt.figure(figsize=(10, 6))


    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {} iteration {}".format(m_curr, b_curr, cost, i))

        plt.plot(x, y_predicted, color="green", alpha=0.5)

    plt.scatter(x, y, color="red", marker="o", label="Data points")
    plt.plot(x, m_curr * x + b_curr, color="blue", label="Final fit line")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Gradient Descent Visualization")
    plt.legend()
    plt.show()

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
