# Given a list of tuples where each tuple contains an expense category (string),
# and an expense amount (float), write a function that returns the expense categories
# with the highest total expenses. The function should take a list of expenses as input
# and a budget as input and return a list of expense categories that have the highest total
# expense.
def calculate_expenses(expenses):
    # Create a dictionary to store the total expenses for each category
    expenses_dict = {}
    # Loop through the expenses list
    for expense in expenses:
        # If the category is not in the dictionary, add it with the expense amount
        if expense[0] not in expenses_dict:
            expenses_dict[expense[0]] = expense[1]
        # If the category is in the dictionary, add the expense amount to the existing total
        else:
            expenses_dict[expense[0]] += expense[1]
    # So for example: Food = 12.5 + 7.5 + 10.0 = 30.0, Transport = 15.0 + 10.0 = 25.0, Accommodation = 50.0
    # Now we have the list of all the expenses, we can find the highest total expense
    highest_expense = max(expenses_dict.values())
    # Now that we have the highest expense value from each category.
    # What is left to do is to get the name that corresponds to the highest expense value
    # Create a list to store the categories with the highest total expenses
    highest_categories = []
    # Loop through the dictionary
    for category, total_expense in expenses_dict.items():
        # If the total expense is equal to the highest expense, add the category to the list
        if total_expense == highest_expense:
            highest_categories.append(category)
    
    return expenses_dict, highest_categories



expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))
expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))
