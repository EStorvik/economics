class Loan():
    """
    Class for calculating the cost of a loan

    Attributes:
        interest (float): the interest rate of the loan
        start_loan (float): the starting loan
        loan (float): the current loan
        interest_payed (float): the total interest payed
        inflation (float): the inflation rate
        inflation_adjusted_interest_payed (float): the interest payed adjusted for inflation
        downpayment_time (int): the time it takes to pay the loan
        month (int): the current month
        year (int): the current year
        gain_from_delayed_payments (float): the gain from delayed payments
        saved_on_taxes (float): the saved money on taxes
        monthly_pay (float): the monthly payment
    """

    def __init__(self, interest: float, start_loan: float, downpayment_time: int, inflation: float = 5.5, start_year: int = 0, start_month: int = 1):
        """
        Constructor for the Loan class

        Args:
            interest (float): the interest rate of the loan
            start_loan (float): the starting loan
            downpayment_time (int): the time it takes to pay the loan
            inflation (float): the inflation rate
            start_year (int): the starting year
            start_month (int): the starting month
        """
        self.interest = interest
        self.start_loan = start_loan
        self.loan = start_loan
        self.interest_payed = 0
        self.inflation = inflation
        self.inflation_adjusted_interest_payed = 0
        self.downpayment_time = downpayment_time
        self.month = start_month
        self.year = start_year
        self.gain_from_delayed_payments = 0
        self.saved_on_taxes = 0
        self.monthly_pay = self.monthly_payment()

    def monthly_payment(self):
        """
        Calculates the monthly payment of the loan
        """
        monthly_rate = self.interest / 12 / 100
        xi = 1+monthly_rate
        num_months = 12*self.downpayment_time
        montly_payments = self.start_loan*xi**num_months*(1-xi)/(1-xi**num_months)
        return montly_payments
    
    def downpayment(self, downpayment):
        """
        Calculates the remaining loan after a downpayment
        
        Args:
            downpayment (float): the downpayment        
        """
        remaining_time = self.downpayment_time-self.year
        self.loan = self.loan - downpayment
        monthly_rate = self.interest / 12 / 100
        xi = 1+monthly_rate
        num_months = 12*remaining_time
        self.montly_pay = self.loan*xi**num_months*(1-xi)/(1-xi**num_months)
        


    def increment_month(self):
        """
        increments the month and updates the loan
        """
        if self.loan >0:

            ip = self.loan * self.interest/100/12
            payback = self.monthly_pay-ip
            self.loan -= payback
            self.interest_payed += ip

            self.saved_on_taxes += ip*0.22/((1-self.inflation)**self.year)

            self.gain_from_delayed_payments += payback*(1-1/((1+self.inflation/100)**self.year))

            self.inflation_adjusted_interest_payed += ip/((1+self.inflation/100)**self.year)
            self.month += 1

            if self.month == 13:
                self.month = 1
                self.year += 1

    def adjusted_cost(self):
        """
        Calculates the adjusted cost of the loan
        """
        return self.inflation_adjusted_interest_payed-self.gain_from_delayed_payments-self.saved_on_taxes