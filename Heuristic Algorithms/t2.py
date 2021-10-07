import numpy as np
import matplotlib.pyplot as plt

# overly-simplified reservoir simulation

# Set some parameters
K = 975 # capacity, TAF
D = 5 # target demand, TAF/day

def cfs_to_taf(Q):
  return Q * 2.29568411*10**-5 * 86400 / 1000

# data setup
Q = np.loadtxt('folsom-data.csv', delimiter=',', skiprows=1, usecols=[4])
Q = cfs_to_taf(Q)
T = len(Q)

S = np.zeros(T)
R = np.zeros(T)
shortage = np.zeros(T)

S[0] = 0.33*K # start simulation full

for t in range(1,T):

  # new storage: mass balance, max value is K
  S[t] = min(S[t-1] + Q[t-1] - R[t-1], K)

  # release is based on demand
  if S[t] + Q[t] > D:
    R[t] = D
  else:
    R[t] = S[t] + Q[t]

  shortage[t] = D-R[t]


reliability = R[R==D].size / float(T)
print(reliability)

# # just plotting below here
plt.subplot(3,1,1)
plt.plot(S)
plt.ylabel('Storage (TAF)')

plt.subplot(3,1,2)
plt.plot(Q, color='steelblue')
plt.plot(R, color='indianred')
plt.legend(['Inflow', 'Delivery'])
plt.ylabel('Flow (TAF/day)')

plt.subplot(3,1,3)
plt.plot(shortage, color='seagreen')
plt.ylabel('Shortage (TAF/day)')
plt.xlabel('Days (from 10/1/2000)')
plt.show()