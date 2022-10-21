class FourSquare():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.investment = 0
        self.cash_flow = 0

    def findIncome(self):
        rent = int(input("How much would you charge per month in rent? "))
        self.income += rent
        misc = int(input("Add any other income from the property - "))
        self.income += misc
        print(f"Okay your total income for this property is {self.income}")
        
    
    def findExpenses(self):
        mortgage = int(input("What will the mortgage payments be per month on this property? "))
        self.expenses += mortgage
        tax_utilities = int(input("How much is the monthly tax payments and the average monthly utility charge? "))
        self.expenses += tax_utilities
        rainy_day = int(input("You will need to set aside money for repairs and vacancy. How much per month will you save? "))
        self.expenses += rainy_day
        property_man = input("Do you plan on having a propert manager? yes or no --> ")
        if property_man == 'yes':
            print(f"We will calculate the managers pay by taking 10% from the total income.")
            manager_pay = self.income * .1
            self.expenses += manager_pay
            print(f"Okay your total expenses are {self.expenses}")
        else:
            print(f"Okay your total expenses are {self.expenses}")

    def showCash_flow(self):
        self.cash_flow = self.income - self.expenses
        print(f"This property is making {self.cash_flow}/month")

    def findInvestment(self):
        down_payment = int(input("What would be the down payment for this property? "))
        self.investment += down_payment
        closing_costs = int(input("What are the closing costs for the investment property? "))
        self.investment += closing_costs
        rehab = input("Do you plan on fixing the place up before you rent it? yes or no --> ")
        if rehab == 'yes':
            budget = int(input("What is your rehab budget? "))
            self.investment += budget
            print(f"Okay your total investment is ${self.investment}")
        else:
            print(f"Okay your total investment is ${self.investment}")

    def showROI(self):
        ROI = ((self.cash_flow * 12) / self.investment) * 100
        ROI = "{0:.2f}".format(ROI)
        print(f"This property has a cash on cash Return On Investment (ROI) of {ROI}%")

        
property = FourSquare()

while True:
    
    property.findIncome()
    property.findExpenses()
    property.showCash_flow()
    property.findInvestment()
    property.showROI()
    break


