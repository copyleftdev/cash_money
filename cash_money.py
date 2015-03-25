# This file is the program that interacts with the user and utilizes person.py's individual class.
import monthly
import hourly_calculator
import household
import time

print "============================================="
print "Monthly expenditure report v1.0 by Danny Chen"
print "=============================================", "\n"


def main_menu():
    print "=============================================", "\n"
    print "Main Menu:"
    print "What would you like to do?: "
    print "1. Make a new household"
    print "2. Load a previous household    ", "\n"
    print "=============================================", "\n"
    action_choice = raw_input("Please choose: ")

    if action_choice == "1":
        print "Created new household."
        new_household()
    else:
        print "Please choose one of the above"
        main_menu()


def family_menu():
    print "=============================================", "\n"
    print family.name + "'s family. Main Menu:"
    print "=============================================", "\n"
    print "1. Add a new family member"
    print "2. Remove a family member"
    print "3. Edit a family member"
    print "4. Show family info"
    print "5. Rename family"
    print "6. Save family"
    print "7. Create Report"
    print "8. Main Menu"
    print "=============================================", "\n"

    while True:
        try:
            family_menu_choice = int(raw_input("Please choose a number: \n"))
            break
        except ValueError:
            print "not a number"

    if family_menu_choice == 1:
        new_family_member()
        family_menu()
    elif family_menu_choice == 2:
        remove_family_member()
        family_menu()
    elif family_menu_choice == 3:
        #edit family member, this will add expenditures, probably pretty complicated
        family_menu()
    elif family_menu_choice == 4:
        family.show_info()
        raw_input("Press enter to continue: ")
    elif family_menu_choice == 5:
        family.name = raw_input("What is your new family name?:")
        print "This is the " + family.name + " household"
        raw_input("press enter to continue")
        family_menu()
    elif family_menu_choice == 6:
        #Save family
        family_menu()
    elif family_menu_choice == 7:
        #create report
        family_menu()
    elif family_menu_choice == 8:
        main_menu()
    else:
        "Please choose from the above choices"
        family_menu()


# Family is initialized. When load function is enabled it will read some csv and initialize the new "family"
def new_household():
    global family
    household_name = raw_input("Please name your household: ")

    family = household.Household(household_name)
    print "---------------------------------------------", "\n"
    family_menu()


def new_family_member():
    # if hourly then plugs into the hourly class, if salaried then directly plug into monthly class
    print "---------------------------------------------"
    print "New family member"
    print "---------------------------------------------"
    print "\n"
    print "Are you hourly or salaried?"
    print "1. Hourly"
    print "2. Salaried"
    print "3. No income"
    print "---------------------------------------------"

    while True:
        global menu_choice
        try:
            menu_choice = int(raw_input("Please choose a number: "))
            break
        except ValueError:
            print "not a number"
            new_family_member()

    if menu_choice == 1:
        while True:
            global hourly_rate
            try:
                hourly_rate = float(raw_input("Hourly Rate: "))
                break
            except ValueError:
                print "not a number"

        while True:
            global weekly_hrs
            try:
                weekly_hrs = float(raw_input("Hours worked per week: "))
                break
            except ValueError:
                print "not a number"
        name = raw_input("What is your name?: ")
        pay = hourly_calculator.HourlyCalculator(hourly_rate, weekly_hrs)
        new_person = monthly.MonthlyIncome(name, pay.monthly_income)
        #debug calculations
        # print 'pay.hours_per_week'
        # print pay.hours_per_week
        # print "\n"
        # print 'pay.monthly_income'
        # print pay.monthly_income
        # print '\n'
        # print 'pay.weekly_income'
        # print pay.weekly_income
        # print '\n'
        # print "new_person.montly_income"
        # print new_person.monthly_income
        # print '\n'
        # print "new_person.yearly_income"
        # print new_person.yearly_income
        # print '\n'
        family.members.append([new_person.name, new_person.monthly_income, new_person.monthly_expenditure])
        print "\n"
        print name + " added!"
        raw_input("Press enter to continue...")
        family_menu()
    elif menu_choice == 2:
        while True:
            global salary
            try:
                salary = float(raw_input("Yearly Salary: "))
                break
            except ValueError:
                print "not a number"

        name = raw_input("What is your name?: ")
        new_person = monthly.MonthlyIncome(name, salary/12)
        family.members.append([new_person.name, new_person.monthly_income, new_person.monthly_expenditure])
        print "\n"
        print name + " added!"
        raw_input("Press enter to continue:")
        family_menu()
    elif menu_choice == 3:
        name = raw_input("What is your name?: ")
        new_person = monthly.MonthlyIncome(name, 0)
        family.members.append([new_person.name, new_person.monthly_income, new_person.monthly_expenditure])
        print "\n"
        print name + " added!"
        raw_input("Press enter to continue:")
        family_menu()


def remove_family_member():
    print "Who would you like to delete?: "
    for i in family.members:
        print str(i[0]) + ": income = " + str(i[1]) + ", expenditure = " + str(i[2])

    name = raw_input("Please enter a name: ")

    for i in family.members:
        if name in i:
            family.members.remove(i)

    print name + " has been deleted from the " + family.name + " family!"
    raw_input("Press enter to continue: ")
    family_menu()


main_menu()