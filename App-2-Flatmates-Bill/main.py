from bill import Bill, Flatmate
from receipt import PdfReport

# CLI functions to collect info
amount = float(input("Enter the amount of the bill: "))
period = input("What is the bill period? E.g. December 2021 ")

name1 = input("What is your name?\n")
days_in_house1 = int(input(f"What many days did {name1} stay in house\n"))

name2 = input("Others name flatmate?\n")
days_in_house2 = int(input(f"What many days did {name2} stay in house\n"))

# create object instant
total_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

# generate pdf report
report = PdfReport(filename="Report Monthly.pdf")
report.generate(flatmate1, flatmate2, total_bill)

print(f"{flatmate1.name} pays: ", flatmate1.pays(total_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(total_bill, flatmate1))
