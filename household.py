import monthly

class Household():
    def __init__(self, name):
        self.name = name
        '''
         for members remember to do a tuple of the
         [earner name, monthly income, monthly expenditure]
         example: (["joe", 2345, 1121], ["schmoe", 1234, 1000])
        '''
        self.members = []
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
            for i in self.members: print str(i[0]) + " makes " + str(i[1]) + " per month.\n"
            print "The household makes " + str(self.monthly_income) + " per month"
            print "and spends " + str(self.monthly_expenditure) + " per month."
            print str(self.monthly_remainder) + " is left per month."
            print "---------------------------------------------\n"
        elif choice == 2:
            print "---------------------------------------------\n"
            print "The " + self.name + " household:\n"
            print "There are " + str(len(self.members)) + " incomes."
            for i in self.members: print str(i[0]) + " makes " + str(i[1] * 12) + " per year.\n"
            print "The household makes " + str(self.yearly_income) + " per year"
            print "and spends " + str(self.yearly_expenditure) + " per year."
            print str(self.yearly_remainder) + " is left per year."
            print "---------------------------------------------\n"

    def household_yearly_calculator(self):
        # resets all calculations, all calculations should be based on the monthly money
        self.monthly_income = 0
        self.monthly_expenditure = 0
        self.yearly_income = 0
        self.yearly_expenditure = 0
        self.yearly_remainder = 0

        for i in self.members:
            self.monthly_income += i[1]
            self.monthly_expenditure += i[2]

        self.yearly_income = self.monthly_income * 12
        self.yearly_expenditure = self.monthly_expenditure * 12
        self.monthly_remainder = self.monthly_income - self.monthly_expenditure
        self.yearly_remainder = self.yearly_income - self.yearly_expenditure
