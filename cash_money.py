# This file is the program that interacts with the user and utilizes
# person.py's individual class.
import hourly_calculator
import household
import time
import os
import pickle

print "============================================="
print "Monthly expenditure report v1.0 by Danny Chen"


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
    elif action_choice == "2":
        load_family()
    else:
        print "Please choose one of the above"
        main_menu()


def family_menu():
    print "=============================================", "\n"
    print family.name + "'s family. Main Menu:"
    print "=============================================", "\n"
    print "1. Add a new family member"
    print "2. Remove a family member"
    print "3. Edit a family member/Add Expenditures"
    print "4. Show family info"
    print "5. Rename family"
    print "6. Save family"
    print ". Main Menu"
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
        edit_member()
    elif family_menu_choice == 4:
        family.show_info()
        raw_input("Press enter to continue: ")
        family_menu()
    elif family_menu_choice == 5:
        family.name = raw_input("What is your new family name?:")
        print "This is the " + family.name + " household"
        raw_input("press enter to continue")
        family_menu()
    elif family_menu_choice == 6:
        family.save_family()
        family_menu()
    elif family_menu_choice == 7:
        main_menu()
    else:
        "Please choose from the above choices"
        family_menu()


def edit_member():
    # this needs to be able to edit name, income, and add expenditures.
    print "\nWhich family member would you like to edit?"
    print "---------------------------------------------"
    for key in family.members:
        print key
    print "cancel"
    print "---------------------------------------------"

    member_str = raw_input("Please enter a name: \n")
    if member_str in family.members:
        member_choice = family.members[member_str]
        # new menu to edit each member dictionary entry.

        def edit_member_menu():
            print "---------------------------------------------"
            print "Monthly Income " + str(format(member_choice[0], '.2f'))
            print "Monthly Expenditures: "
            for key, val in member_choice[1].items():
                print key + ": " + str(val)
            print "---------------------------------------------"
            print "1. Add Expenditure"
            print "2. Remove Expenditure"
            print "3. Change Income"
            print "4. Change Name"
            print "5. Return"
            print "---------------------------------------------"

            while True:
                global member_menu_choice
                try:
                    member_menu_choice = int(
                        raw_input("Please choose a number: \n"))
                    break
                except ValueError:
                    print "not a number"

            # adding expenditure
            if member_menu_choice == 1:
                expenditure_name = raw_input("What is the expenditure name?: ")
                while True:
                    global expenditure_amount
                    try:
                        expenditure_amount = int(
                            raw_input("What is the expenditure amount?: \n"))
                        break
                    except ValueError:
                        print "not a number"
                member_choice[1][expenditure_name] = expenditure_amount
                edit_member_menu()

            # deleting expenditure
            elif member_menu_choice == 2:
                print "---------------------------------------------"
                for key, val in member_choice[1].items():
                    print key + ": " + str(val)
                while True:
                    expenditure_to_delete = raw_input(
                        "\nWhich expenditure to delete?: ")
                    if expenditure_to_delete in member_choice[1]:
                        del member_choice[1][expenditure_to_delete]
                        print expenditure_to_delete + " Deleted!\n"
                        break
                    print "Expenditure not found, try again"
                edit_member_menu()

            # changing income amount
            elif member_menu_choice == 3:
                print "---------------------------------------------"
                print "Changing " + member_str + " income: "
                print "Are you hourly or salaried?"
                print "1. Hourly"
                print "2. Salaried"
                print "3. No income"
                print "---------------------------------------------"

                while True:
                    global menu_choice
                    try:
                        menu_choice = int(
                            raw_input("Please choose a number: "))
                        break
                    except ValueError:
                        print "not a number"

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
                            weekly_hrs = float(
                                raw_input("Hours worked per week: "))
                            break
                        except ValueError:
                            print "not a number"
                    pay = hourly_calculator.HourlyCalculator(
                        hourly_rate, weekly_hrs)
                    member_choice[0] = pay.monthly_income
                elif menu_choice == 2:
                    while True:
                        global salary
                        try:
                            salary = float(raw_input("Yearly Salary: "))
                            break
                        except ValueError:
                            print "not a number"
                    member_choice[0] = salary / 12
                print "Income changed. New Monthly income: " + str(format(member_choice[0], '.2f'))
                edit_member_menu()

            # changing name of current member
            elif member_menu_choice == 4:
                new_name = raw_input("What is your new name?: \n")
                family.members[new_name] = family.members[member_str]
                del family.members[member_str]
                print member_str + " renamed to " + new_name + "!"
                raw_input("Press enter to continue")
                edit_member()

            # return to family menu
            elif member_menu_choice == 5:
                family_menu()

            # reprints member menu with selected member
            else:
                print "Not in range"
                edit_member_menu()

        edit_member_menu()
    elif member_str.lower() == "cancel":
        family_menu()
    # this handles when user doesn't enter correct name
    else:
        print "Family Member not found"
        edit_member()


def new_household():
    global family
    household_name = raw_input("Please name your household: ")
    family = household.Household(household_name)
    print "---------------------------------------------", "\n"
    family_menu()


def new_family_member():
    # if hourly then plugs into the hourly class, if salaried then directly
    # plug into monthly class
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

    # hourly employee section
    if menu_choice == 1:
        name = raw_input("What is your name?: ")
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
        pay = hourly_calculator.HourlyCalculator(hourly_rate, weekly_hrs)
        # debug calculations
        # print 'pay.hours_per_week'
        # print pay.hours_per_week
        # print "\n"
        # print 'pay.monthly_income'
        # print pay.monthly_income
        # print '\n'
        # print 'pay.weekly_income'
        # print pay.weekly_income
        # print '\n'
        # print 'pay.biweekly_income'
        # print pay.biweekly_income
        # print '\n'
        # print "new_person.monthly_income"
        # print new_person.monthly_income
        # print '\n'
        # print "new_person.yearly_income"
        # print new_person.yearly_income
        # print '\n'
        family.members[name] = [pay.monthly_income, {}]
        print "\n"
        print name + " added!"
        raw_input("Press enter to continue...")
        family_menu()

    # salary income
    elif menu_choice == 2:
        name = raw_input("What is your name?: ")
        while True:
            global salary
            try:
                salary = float(raw_input("Yearly Salary: "))
                break
            except ValueError:
                print "not a number"

        family.members[name] = [salary / 12, {}]
        print "\n"
        print name + " added!"
        raw_input("Press enter to continue:")
        family_menu()
    elif menu_choice == 3:
        name = raw_input("What is your name?: ")
        family.members[name] = [0, {}]
        print "\n"
        print name + " added!"
        raw_input("Press enter to continue:")
        family_menu()

    # no income
    else:
        print "\n Please choose from above numbers"
        raw_input("Press enter to continue: ")
        new_family_member()


def remove_family_member():
    print "Who would you like to delete?: "
    for key in family.members:
        print key + ": income = " + str(family.members[key][0]) + ", expenditure = " + str(family.members[key][1])

    name = raw_input("Please enter a name: ")

    if name in family.members:
        del family.members[name]
    else:
        print "---------------------------------------------"
        print "Family Member not found!"
        print "1. Try Again"
        print "2. Return"
        print "---------------------------------------------"

        while True:
            try:
                choice = int(raw_input("\nPlease Choose:"))
                break
            except ValueError:
                print "not a number"

        if choice == 1:
            remove_family_member()
        elif choice == 2:
            family_menu()

    print name + " has been deleted from the " + family.name + " family!"
    raw_input("Press enter to continue: ")
    family_menu()


def load_family():
    files = os.listdir(os.getcwd())
    save_files = []
    # saves are individual files in working directory in .save format, the
    # name of the file is the family name
    for i in files:
        if ".save" in i:
            save_files.append(i)
    if len(save_files) > 0:
        for i in save_files:
            print i
        save_choice = raw_input("Which family would you like to load?: ")

        if save_choice in save_files:
            global family
            family = pickle.load(open(save_choice))
            print save_choice + " loaded!"
            family_menu()
        else:
            print "\n", save_choice + " NOT FOUND"
            main_menu()
    else:
        print "No save files found."
        main_menu()

main_menu()
