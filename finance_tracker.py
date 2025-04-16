import csv
from datetime import datetime
import matplotlib.pyplot as plt

class Transaction:
    def __init__(self, amount, category, date, transaction_type):
        self.amount = float(amount)
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.type = transaction_type  # 'income' or 'expense'

    def __repr__(self):
        return f"{self.date.strftime('%Y-%m-%d')} {self.type}: {self.category} ${self.amount:.2f}"

def load_transactions(filename):
    transactions = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(Transaction(
                row['amount'],
                row['category'],
                row['date'],
                row['type']
            ))
    return transactions

def categorize_spending(transactions):
    categories = {}
    for transaction in transactions:
        if transaction.type == 'expense':
            if transaction.category not in categories:
                categories[transaction.category] = []
            categories[transaction.category].append(transaction)
    return categories

def calculate_budget(income, expenses):
    return sum(t.amount for t in income) - sum(t.amount for t in expenses)

def generate_report(transactions, timeframe='all'):
    now = datetime.now()
    filtered = []
    
    for t in transactions:
        if timeframe == 'month' and t.date.month == now.month:
            filtered.append(t)
        elif timeframe == 'year' and t.date.year == now.year:
            filtered.append(t)
        else:
            filtered.append(t)
    
    income = sum(t.amount for t in filtered if t.type == 'income')
    expenses = sum(t.amount for t in filtered if t.type == 'expense')
    return {
        'total_income': income,
        'total_expenses': expenses,
        'net_savings': income - expenses
    }

def plot_spending(transactions):
    categories = categorize_spending(transactions)
    labels = []
    values = []
    
    for category, transactions in categories.items():
        labels.append(category)
        values.append(sum(t.amount for t in transactions))
    
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.show()

def save_goals(goals):
    with open('financial_goals.txt', 'w') as f:
        for category, amount in goals.items():
            f.write(f"{category}:{amount}\n")

def progress_toward_goal(current, goal):
    return (current / goal) * 100 if goal != 0 else 0

# Main program execution
def main():
    transactions = []
    goals = {}
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Financial Report")
        print("3. Plot Spending")
        print("4. Manage Savings Goals")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            t_type = input("Type (income/expense): ")
            transactions.append(Transaction(amount, category, date, t_type))
            
        elif choice == '2':
            timeframe = input("Report timeframe (month/year/all): ")
            report = generate_report(transactions, timeframe)
            print(f"\nIncome: ${report['total_income']:.2f}")
            print(f"Expenses: ${report['total_expenses']:.2f}")
            print(f"Net Savings: ${report['net_savings']:.2f}")
            
        elif choice == '3':
            plot_spending(transactions)
            
        elif choice == '4':
            goal_category = input("Goal category: ")
            goal_amount = float(input("Target amount: "))
            goals[goal_category] = goal_amount
            save_goals(goals)
            
        elif choice == '5':
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()