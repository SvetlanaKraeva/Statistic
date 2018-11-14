from functions import distribution as dstrb
from functions import structure as strct
import numpy as np
import matplotlib.pyplot as plt


n = [20, 50, 100]
m = 1000


'for i in n:'
measures_1 = strct.Structure_of_measures()
measures_2 = strct.Structure_of_measures()
measures_3 = strct.Structure_of_measures()
measures_4 = strct.Structure_of_measures()
measures_5 = strct.Structure_of_measures()
for j in range(m):
    distribution_1 = np.random.standard_normal(n[1])
    distribution_2 = np.random.laplace(0, 1.0, n[1])
    distribution_3 = np.random.uniform(0, 1.0, n[1])
    distribution_4 = np.random.standard_cauchy(n[1])
    distribution_5 = dstrb.cauchy_normal(n[1])

    measures_1.__add__(distribution_1)
    measures_2.__add__(distribution_2)
    measures_3.__add__(distribution_3)
    measures_4.__add__(distribution_4)
    measures_5.__add__(distribution_5)

Var = np.zeros((5, 10), dtype=float)
Var[0][:] = measures_1.calc_var()
Var[1][:] = measures_2.calc_var()
Var[2][:] = measures_3.calc_var()
Var[3][:] = measures_4.calc_var()
Var[4][:] = measures_5.calc_var()
Var = np.transpose(Var)

Mean = np.zeros((5, 10), dtype=float)
Mean[0][:] = measures_1.calc_mean()
Mean[1][:] = measures_2.calc_mean()
Mean[2][:] = measures_3.calc_mean()
Mean[3][:] = measures_4.calc_mean()
Mean[4][:] = measures_5.calc_mean()
Mean = np.transpose(Mean)

'plt.plotting(distribution_1)'
columns = ['normal', 'laplace', 'uniform', 'cauchy', 'cauchy-normal']
rows = ['mean', 'med', 'z_r', 'z_tr', 'z_q', 'S', 'D', 'R', 'IQR', 'MAD']
print(Var)
print(Mean)






