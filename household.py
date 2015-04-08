import monthly

class Household():
    def __init__(self, name):
        self.name = name
        '''
         for members remember to do a dictionary with earner name as primary key
         and monthly income/expenditures in a list within that key
         {"Name": [Income, Expenditure]}
         example: {"joe": [2345, {"expenditure", 1121}], "schmoe": [1234, {"expenditure", 1000}]}
        '''
        self.members = {}
        self.monthly_income = 0
        self.monthly_expenditure = 0
        self.yearly_income = 0
        self.yearly_expenditure = 0
        self.monthly_remainder = 0
        self.yearly_remainder = 0

    def show_info(self):
        self.household_yearly_calculator()
        print "\n"
        print "1. Monthly Summary"
        print "2. Yearly Summary"

        while True:
            global choice
            try:
                choice = int(raw_input("Please choose a number: "))
                break
            except ValueError:
                print "not a number"

        if choice == 1:
            print "---------------------------------------------\n"
            print "The " + self.name + " household:\n"
            print "There are " + str(len(self.members)) + " incomes."
            for key in self.members: print key + " makes " + str(format(self.members[key][0], '.2f')) + " per month.\n"
            print "The household makes " + str(format(self.monthly_income, '.2f')) + " per month"
            print "and spends " + str(format(self.monthly_expenditure, '.2f')) + " per month."
            print str(format(self.monthly_remainder, '.2f')) + " is left per month."
            print "---------------------------------------------\n"
        elif choice == 2:
            print "---------------------------------------------\n"
            print "The " + self.name + " household:\n"
            print "There are " + str(len(self.members)) + " incomes."
            for key in self.members: print key + " makes " + str(format(self.members[key][0] * 12, '.2f')) + " per year.\n"
            print "The household makes " + str(format(self.yearly_income, '.2f')) + " per year"
            print "and spends " + str(format(self.yearly_expenditure, '.2f')) + " per year."
            print str(format(self.yearly_remainder, '.2f')) + " is left per year."
            print "---------------------------------------------\n"

    def household_yearly_calculator(self):
        # resets all calculations, all calculations should be based on the monthly money
        self.monthly_income = 0
        self.monthly_expenditure = 0
        self.yearly_income = 0
        self.yearly_expenditure = 0
        self.yearly_remainder = 0

        for key in self.members:
            self.monthly_income += self.members[key][0]
            self.monthly_expenditure -= self.members[key][1]

        self.yearly_income = self.monthly_income * 12
        self.yearly_expenditure = self.monthly_expenditure * 12
        self.monthly_remainder = self.monthly_income - self.monthly_expenditure
        self.yearly_remainder = self.yearly_income - self.yearly_expenditure
