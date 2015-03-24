#class Individual will store the name, income, expenditures, and monthly remainders for all adjustments
class MonthlyIncome():
    def __init__(self, name, monthly_income):
        self.name = name
        self.monthly_income = monthly_income
        self.expenditure = 0
        self.remaining = 0
        self.weekly_income = self.monthly_income / 4
        self.yearly_income = self.weekly_income * 52
        self.yearly_expenditure = self.expenditure * 12

    def show_info(self):
        print "---------------------------------------------"
        print self.name+": "
        print "Monthly Income: " + str(self.monthly_income)
        print "Monthly Expenditures: "+ str(self.expenditure)
        print "Monthly Remainder: "+ str(self.remaining)
        print "---------------------------------------------"

    def add_income(self, new_income):
        self.monthly_income += new_income
        print "Income added, total income: "+str(self.monthly_income) + "\n"
        self.calculate_remaining()

    def add_expenditure(self, new_expenditure):
        self.expenditure += new_expenditure
        print "Expenditure added, total expenditure: "+str(self.expenditure) + "\n"
        self.calculate_remaining()

    def calculate_remaining(self):
        self.remaining = self.monthly_income - self.expenditure