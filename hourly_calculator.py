#calculates hourly, weekly, biweekly, monthly, yearly income
class HourlyCalculator():
    def __init__(self, hourly_rate, hours_per_week):
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week
        self.weekly_income = 0
        self.biweekly_income = 0
        self.monthly_income = 0
        self.calculate()

    def show_info(self):
        self.calculate()
        print "Hourly Rate: " + str(self.hourly_rate)
        print "Weekly Pay: " + str(self.weekly_income)
        print "Biweekly Pay: " + str(self.biweekly_income)
        print "Monthly Income: " + str(self.monthly_income)

    def calculate(self):
        #credit sierra shorey for overtime calculator
        if self.hours_per_week <= 40:
            self.weekly_income = self.hourly_rate * self.hours_per_week
        elif self.hours_per_week > 40:
            self.weekly_income = self.hourly_rate * 40 + (self.hourly_rate * 1.5 * (self.hours_per_week - 40))

        self.biweekly_income = self.weekly_income * 2
        self.monthly_income = self.biweekly_income * 2
