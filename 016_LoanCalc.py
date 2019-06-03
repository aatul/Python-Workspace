print("Enter Loan Amount")
loan_amount = input()
la = float(loan_amount)

print("Enter Rate of Interest")
rate_of_interest = input()
roi = float(rate_of_interest)

print("Enter Loan Period")
loan_period = input()
lp = float(loan_period)

emi =  (la * roi * lp)/100
print(emi)

total_amount = emi * lp
print(total_amount)