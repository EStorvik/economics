class Account():
    """
    Class for a savings account.

    Attributes:
        interest (float): the interest rate of the account
        start_money (float): the starting money in the account
        money (float): the current money in the account
        inflation_adjusted_money (float): the current money in the account adjusted for inflation
        year (int): the current year
        inflation (float): the inflation rate
    """

    def __init__(self, interest: float, start_money: float, inflation: float = 5.5, start_year: int = 0) -> None:
        """
        Constructor for the Account class
        
        Args:
            interest (float): the interest rate of the account
            start_money (float): the starting money in the account
            inflation (float): the inflation rate
            start_year (int): the starting year
        """

        self.interest = interest
        self.start_money = start_money
        self.money = start_money
        self.inflation_adjusted_money = start_money
        self.inflation = inflation
        self.year = start_year

    def increment_year(self):
        """
        Increments the year and updates the money in the account
        """
        self.year += 1
        self.money *= (1+self.interest/100)
        self.inflation_adjusted_money = self.money/(1+self.inflation/100)**self.year
    
    def adjusted_change(self):
        """
        Calculates the change in the account adjusted for inflation
        """
        return self.inflation_adjusted_money-self.start_money

