import monthly

class Household():
    def __init__(self, name, earners):
        self.name = name
        self.earners = earners
        '''
         for members remember to do a tuple of the
         [earner name, yearly income, yearly expenditure]
         example: (["joe", 23456, 11214], ["schmoe", 12345, 10001])
        '''
        self.members = []
        self.yearly_income = 0
        self.yearly_expenditure = 0
        self.remainder = 0
        self.household_yearly_calculator()

    def show_info(self):
        print "---------------------------------------------"
        print "The " + self.name + " household:"
        print "There are " + str(self.earners) + " incomes."
        for i in self.members: print str(i[0]) + " makes " + str(i[1]) + " per year."
        print "The household makes " + str(self.yearly_income) + " per year"
        print "and spends " + str(self.yearly_expenditure) + " per year."
        print str(self.remainder) + " is left per year."
        print "---------------------------------------------"

    def household_yearly_calculator(self):

        # adds all incomes and expenditures for each member to self.yearly_income and self.yearly_expenditure
        for i in self.members:
            self.yearly_income += i[1]
            self.yearly_expenditure += i[2]

        self.remainder = self.yearly_income - self.yearly_expenditure
