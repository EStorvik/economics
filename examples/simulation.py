
from economics import Loan, Account, Fund

import numpy as np
import matplotlib.pyplot as plt



money_bank = 100000
interest_bank = 4

money_loan = 100000
interest_loan = 5.5

money_fund = 100000
interest_fund = 10

inflation = 4.3
years = 20


bank = Account(interest=interest_bank, start_money=money_bank, inflation=inflation)
lån = Loan(interest=interest_loan, start_loan=money_loan, downpayment_time= years, inflation=inflation)
fund = Fund(return_percentage=interest_fund, start_money=money_fund, inflation=inflation)



t = np.linspace(0,years, years)
b = []
l = []
c_l = []
f = []


for i in range(years):
    bank.increment_year()
    fund.increment_year()
    for j in range(12):
        lån.increment_month()
    b.append(bank.adjusted_change())
    l.append(lån.loan)
    c_l.append(lån.adjusted_cost())
    f.append(fund.adjusted_change())


plt.figure()
plt.plot(t, b)
plt.legend(["Value change of money in bank"])
plt.figure()
plt.plot(t, c_l)
plt.legend(["inflation adjusted cost of loan"])
plt.figure()
plt.plot(t, f)
plt.legend(["inflation (and tax) adjusted change of money in fund"])
plt.show()

