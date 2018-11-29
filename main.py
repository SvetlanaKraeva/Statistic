from functions import distribution as dstrb
from functions import structure as strct
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from IPython.display import display, Markdown, Latex

n = [20, 50, 100]
m = 1000
names = ['normal', 'laplace', 'uniform', 'cauchy', 'cauchy-normal']
meas = ['mean', 'med', 'z_r', 'z_tr', 'z_q', 'S', 'D', 'R', 'IQR', 'MAD']
meas = ['mean', 'med', 'z_r', 'z_tr', 'z_q']
for i in n:
    measures_1 = strct.Structure_of_measures()
    measures_2 = strct.Structure_of_measures()
    measures_3 = strct.Structure_of_measures()
    measures_4 = strct.Structure_of_measures()
    measures_5 = strct.Structure_of_measures()
    sample = np.zeros((5, i), dtype=float)
    measures = np.zeros((5, len(meas)), dtype=float)
    cycol = cycle('kbgrcmy')

    for j in range(m):
        distribution_1 = np.random.standard_normal(i)
        distribution_2 = np.random.laplace(0, 1.0, i)
        distribution_3 = np.random.uniform(0, 1.0, i)
        distribution_4 = np.random.standard_cauchy(i)
        distribution_5 = dstrb.cauchy_normal(i)

        measures_1.__add__(distribution_1)
        measures_2.__add__(distribution_2)
        measures_3.__add__(distribution_3)
        measures_4.__add__(distribution_4)
        measures_5.__add__(distribution_5)
        if j == 100:
            sample[0][:] = distribution_1
            sample[1][:] = distribution_2
            sample[2][:] = distribution_3
            sample[3][:] = distribution_4
            sample[4][:] = distribution_5
            measures[0][:] = measures_1.out(j)
            measures[1][:] = measures_2.out(j)
            measures[2][:] = measures_3.out(j)
            measures[3][:] = measures_4.out(j)
            measures[4][:] = measures_5.out(j)


    Var = np.zeros((5, len(meas)), dtype=float)
    Var[0][:] = measures_1.calc_var()
    Var[1][:] = measures_2.calc_var()
    Var[2][:] = measures_3.calc_var()
    Var[3][:] = measures_4.calc_var()
    Var[4][:] = measures_5.calc_var()
    Var = np.transpose(Var)

    Mean = np.zeros((5, len(meas)), dtype=float)
    Mean[0][:] = measures_1.calc_mean()
    Mean[1][:] = measures_2.calc_mean()
    Mean[2][:] = measures_3.calc_mean()
    Mean[3][:] = measures_4.calc_mean()
    Mean[4][:] = measures_5.calc_mean()
    Mean = np.transpose(Mean)

    for j in range(len(names)):
        with open('output/' + names[j] + str(i)+'.txt', "w+") as text:
            text.write('{:>10}: {:>10}: {:>10}:'.format('Measure', 'mean', 'variance')+'\n')
            for k in range(len(meas)):
                text.write('{:>10}: {:>10} {:>10}'.format(meas[k], str('%.5f' % Mean[k][j]), str('%.5f' % Var[k][j]))+'\n')
        text.close()

        plt.figure()
        plt.hist(sample[j][:],  histtype='bar', bins=i, alpha=0.75)
        plt.title('{} - {:d} samples'.format(names[j], i))
        plt.tight_layout()
        plt.grid(True)
        for k in range(len(meas)):
            plt.axvline(x=measures[j][k], label='{:<5} {:<5}'.format(meas[k], str('%.5f' % measures[j][k])), c=next(cycol))
        plt.legend()
        plt.boxplot(sample[j][:], vert=False)
        plt.savefig('output/{}_{:d}.png'.format(names[j], i), bbox_inches='tight')
        plt.close()


