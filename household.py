import pickle
import os


class Household():

    def __init__(self, name):
        self.name = name
        '''
         for members remember to do a dictionary with earner name as
         primary key and monthly_income/monthly_expenditures in a
         dictionary within that key
         {"Name": [income, {expenditure_name, expenditure}]}
         example:
         {"joe": [2345, {"expenditure", 1121}], "schmoe": [1234,
         {"expenditure", 1000}]}
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
            print "There are " + str(len(self.members)) + " incomes.\n"
            for each in self.members:
                print each + " makes " + str(format(self.members[each][0],
                                                    '.2f')) + " per month."
                if len(self.members[each][1]) == 0:
                    print each + " has no expenditures.\n"
                else:
                    print each + "'s " + "expenditures:"
                    for key, value in self.members[each][1].items():
                        print key + ": " + str(format(value, ".2f"))
                    print "\n"
            print "\nThe household makes " + str(format(self.monthly_income,
                                                        '.2f')) + " per month"
            print "and spends " + str(format(self.monthly_expenditure,
                                             '.2f')) + " per month."
            print str(format(self.monthly_remainder,
                             '.2f')) + " is left per month."
            print "---------------------------------------------\n"
        elif choice == 2:
            print "---------------------------------------------\n"
            print "The " + self.name + " household:\n"
            print "There are " + str(len(self.members)) + " incomes.\n"
            for each in self.members:
                print each + " makes " +
                str(format(self.members[each][0] * 12, '.2f')) + " per year."
                if len(self.members[each][1]) == 0:
                    print each + " has no expenditures.\n"
                else:
                    for key, value in self.members[each][1].items():
                        print key + ": " + str(format(value * 12, ".2f"))
                    print "\n"
            print "\nThe household makes " + str(format(self.yearly_income,
                                                        '.2f')) + " per year"
            print "and spends " + str(format(self.yearly_expenditure,
                                             '.2f')) + " per year."
            print str(format(self.yearly_remainder,
                             '.2f')) + " is left per year."
            print "---------------------------------------------\n"

    def household_yearly_calculator(self):
        # resets all calculations, all calculations should be based on the
        # monthly money
        self.monthly_income = 0
        self.monthly_expenditure = 0
        self.yearly_income = 0
        self.yearly_expenditure = 0
        self.yearly_remainder = 0

        for key, value in self.members.items():
            self.monthly_income += value[0]
            for x in value[1].values():
                self.monthly_expenditure += x

        self.yearly_income = self.monthly_income * 12
        self.yearly_expenditure = self.monthly_expenditure * 12
        self.monthly_remainder = self.monthly_income - self.monthly_expenditure
        self.yearly_remainder = self.yearly_income - self.yearly_expenditure

    def save_family(self):
        # json.dump(self.mem bers, open(self.name + ".save", "a+"))
        if self.name + ".save" in os.listdir(os.getcwd()):
            os.remove(self.name + ".save")
            pickle.dump(self, open(self.name + ".save", "w+"))
        else:
            pickle.dump(self, open(self.name + ".save", "w+"))

        print "family saved"
        raw_input("Press Enter to continue:")
