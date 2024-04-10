
# Unit mid2 activity 
# Tony Du
# April 8, 2024 

# function that calculates total spendings for a month
def calculate_total_spending(expenses):
    """
    Calculate the total spending for the month from a list of expenses.

    Parameters:
    expenses (list): A list containing the expenses for each day of the month.

    Returns:
    float: The total spending for the month.
    """
    total_spending = sum(expenses)
    return total_spending

if __name__ == "__main__":
    # Input daily expenses using a loop
    num_days = 30  # Assuming a month has 30 days
    daily_expenses = []

    for day in range(1, num_days + 1):
        expense = float(input(f"Enter expenses for day {day}: "))
        daily_expenses.append(expense)

    # Calculate total spending for the month
    total_monthly_spending = calculate_total_spending(daily_expenses)
    print("Total spending for the month:", total_monthly_spending)