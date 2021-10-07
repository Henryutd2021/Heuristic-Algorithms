# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
#
# data = {'SA':[91.94,
# 77.13,
# 10.93,
# 18.6,
# 28.63,
# 86.52,
# 64.58,
# 22.23,
# 59.75,
# 134.11,
# ], 'GA':[147.9,
# 97.88,
# 39.76,
# 204.48,
# 488.83,
# 113,
# 141.97,
# 53.76,
# 408.2,
# 226.95,
# ], 'GS':[47.66,
# 150.53,
# 97.04,
# 82.62,
# 99.89,
# 76.52,
# 87.84,
# 51.73,
# 147.51,
# 115.98
# ]}
#
# df = pd.DataFrame(data,
# columns=['SA', 'GA', 'GS'])
# df.boxplot(sym='r*',vert=True,patch_artist=False,meanline=True,showmeans=True)
#
# plt.show()


# import numpy as np
# import statsmodels.api as sm
# import matplotlib.pyplot as plt
#
# sample = [{'SA':[91.94,
# 77.13,
# 10.93,
# 18.6,
# 28.63,
# 86.52,
# 64.58,
# 22.23,
# 59.75,
# 134.11,
# ]}, {'GA':[147.9,
# 97.88,
# 39.76,
# 204.48,
# 488.83,
# 113,
# 141.97,
# 53.76,
# 408.2,
# 226.95
# ]}, {'GS': [47.66,
# 150.53,
# 97.04,
# 82.62,
# 99.89,
# 76.52,
# 87.84,
# 51.73,
# 147.51,
# 115.98
# ]}]
# for i in sample:
#     for k, j in i.items():
#         ecdf = sm.distributions.ECDF(j)
#         x = np.linspace(min(j), max(j))
#         y = ecdf(x)
#         plt.step(x, y, label=k)
#
# plt.title('Empirical CDF function')
# plt.xlabel('Objective Function Value')
# plt.ylabel('Culumative Probability')
# plt.legend()
# plt.show()


from scipy import stats


SA = [91.94, 77.13, 10.93, 18.6, 28.63, 86.52, 64.58, 22.23, 59.75, 134.11]
GA = [147.9, 97.88, 39.76, 204.48, 488.83, 113, 141.97, 53.76, 408.2, 226.95]
GS = [47.66, 150.53, 97.04, 82.62, 99.89, 76.52, 87.84, 51.73, 147.51, 115.98]
# t = stats.levene(GA, GS)
# T = stats.ttest_ind(GA, GS, equal_var=False)
# #T1 = stats.ttest_rel(GA, GS)
# print(T)
# #print(T1)
# print(t)

# Example of the Mann-Whitney U Test
from scipy.stats import pearsonr
# data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
# data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = pearsonr(GA, GS)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')











