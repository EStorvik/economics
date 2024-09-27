from economics import Account

import numpy as np
import matplotlib.pyplot as plt

start = 100000
interest = 4


bank = Account(interest=interest, start_money=start)

years = 20

t = np.linspace(0,years, years)
m = []

for i in range(years):
    bank.increment_year()
    m.append(bank.money)


plt.figure()
plt.plot(t, m)
plt.show()