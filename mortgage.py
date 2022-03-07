#Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan.

def mortgage_total(amount_of_credit, percentage):
    
    return ((amount_of_credit*percentage)/100)+amount_of_credit
    
def number_of_repayment_periods(period):
    
    return period
        
def main():
    
    amount_of_credit = float(input("Enter the loan amount: "))
    percentage = float(input("Enter percentage of the loan: "))
    total = mortgage_total(amount_of_credit, percentage)
    
    period = int(input("How many instalments you want to have (in months): "))
    your_period = number_of_repayment_periods(period)
    
    repayment = round(total/your_period,2)
    
    print(f"Total cost {total} your repayment is {repayment} in {your_period} months.")
    
if __name__ == "__main__":
    main()
