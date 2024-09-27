from economics import Loan

import numpy as np
import matplotlib.pyplot as plt

start = 100000
interest = 5.62
years = 20

lån = Loan(interest=interest, start_loan=start, downpayment_time=years)

t = np.linspace(0,years, years)
l = []
c = []
for i in range(years):
    for j in range(12):
        lån.increment_month()

    l.append(lån.loan)
    c.append(lån.interest_payed)

plt.figure()
plt.plot(t,l)
plt.plot(t, c)
plt.legend(["loan", "interest payed"])
plt.show()