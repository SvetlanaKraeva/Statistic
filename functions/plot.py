import matplotlib.pyplot as plt


def plotting(distribution):
    plt.hist(distribution, bins=1, density=True, facecolor='g')
    plt.show()
