class Fund():
    """
    a class to represent a fund

    Attributes:
        return_percentage (float): the return percentage of the fund
        start_money (float): the starting money in the fund
        inflation (float): the inflation rate
        start_year (int): the starting year
        money (float): the current money in the fund
        inflation_adjusted_money (float): the current money in the fund adjusted for inflation
        year (int): the current year

    """

    def __init__(self, return_percentage: float, start_money: float, inflation: float = 5.5, start_year: int = 0):
        """
        Constructor for the Fund class

        Args:
            return_percentage (float): the return percentage of the fund
            start_money (float): the starting money in the fund
            inflation (float): the inflation rate
            start_year (int): the starting year
        """
        self.return_percentage = return_percentage
        self.start_money = start_money
        self.money = start_money
        self.inflation_adjusted_money = start_money
        self.inflation = inflation
        self.year = start_year
    
    def increment_year(self):
        """
        increments the year and updates the money in the fund
        """
        self.year += 1
        self.money *= (1+self.return_percentage/100)
        self.inflation_adjusted_money = self.money/(1+self.inflation/100)**self.year
    
    def subtractable_money(self,inflation_adjusted = True):
        """
        calculates the money that can be subtracted from the fund
        
        Args:
            inflation_adjusted (bool): if the money should be adjusted for inflation (default is True)
        """
        gain = self.money-self.start_money
        tax_deducted_gain = gain*(1.0-0.3784)
        total_subtractable = tax_deducted_gain+self.start_money
        if inflation_adjusted:
            return total_subtractable/(1+self.inflation/100)**self.year
        else:
            return total_subtractable



        
