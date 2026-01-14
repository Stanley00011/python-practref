
""" Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, 
which calculates the measure of central tendency of a sample (mean, median, mode) and measure of 
variability (range, variance, standard deviation). In addition to those measures, 
find the min, max, count, percentile, and frequency distribution of the sample. 
You can create a class called Statistics and create all the functions that do statistical calculations 
as methods for the Statistics class. Check the output below. """
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        # We sort the data right away to make median and range calculations easier
        self.data = sorted(data)
        self.n = len(self.data)

# Basic Measures 
    def count(self):
        return self.n

    def sum(self):
        return sum(self.data)

    def min(self):
        return self.data[0] # First element of sorted list

    def max(self):
        return self.data[-1] # Last element of sorted list

    def range(self):
        return self.max() - self.min()

    def mean(self):
        # Formula: sum of all items / total number of items
        return round(self.sum() / self.n)

    def median(self):
        # If odd: take the middle one. If even: average the two middle ones.
        mid = self.n // 2
        if self.n % 2 != 0:
            return self.data[mid]
        return (self.data[mid - 1] + self.data[mid]) / 2

    def mode(self):
        # We use Counter to find the frequency of each number
        counts = Counter(self.data)
        # most_common(1) returns a list like [(value, count)]
        top = counts.most_common(1)[0]
        return {'mode': top[0], 'count': top[1]}
    
    def var(self):
        mu = self.mean()
        # 1. For every x in data, find (x - mean) squared
        # 2. Sum those squares
        # 3. Divide by total count
        sum_sq_diff = sum((x - mu) ** 2 for x in self.data)
        return round(sum_sq_diff / self.n, 1)

    def std(self):
        # Standard Deviation is just the square root of Variance
        return round(math.sqrt(self.var()), 1)
    
    def freq_dist(self):
        # Returns a list of (percentage, value) sorted by frequency
        # Formula: (count of specific value / total count) * 100
        counts = Counter(self.data)
        dist = [(round((count / self.n) * 100, 1), val) for val, count in counts.items()]
        # We sort by the percentage (index 0) in descending order
        return sorted(dist, reverse=True)

    def describe(self):
        # This brings it all together into a formatted string
        return (f"Count: {self.count()}\n"
                f"Sum: {self.sum()}\n"
                f"Mean: {self.mean()}\n"
                f"Median: {self.median()}\n"
                f"Mode: {self.mode()}\n"
                f"Variance: {self.var()}\n"
                f"Standard Deviation: {self.std()}\n"
                f"Frequency Distribution: {self.freq_dist()}")
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print(data.describe())


""" Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.
"""

class PersonAccount:
    def __init__(self, firstname, lastname):
        """
        Initializes a new PersonAccount with a first name, last name, 
        and empty lists for incomes and expenses.
        """
        self.firstname = firstname
        self.lastname = lastname
        # Incomes and expenses are stored as lists of dictionaries 
        # where each dictionary has 'description' and 'amount' keys.
        self.incomes = []
        self.expenses = []
    def add_income(self, description, amount):
         #Adds a new income entry to the incomes list
        if amount > 0:
            self.incomes.append({'description': description, 'amount': amount})
        else:
            print("Amount must be positive.")

    def add_expense(self, description, amount):
        # Adds a new expense entry to the expenses list
        if amount > 0:
            self.expenses.append({'description': description, 'amount': amount})
        else:
            print("Amount must be positive.")
    
    def total_income(self):
        # Calculates and returns the total sum of all incomes
        return sum(income['amount'] for income in self.incomes)
    
    def total_expense(self):
        # calculates and returns the total sum of all expenses.
        return sum(expense['amount'] for expense in self.expenses)

    def account_balance(self):
        #Calculates and returns the current account balance (total income - total expense)
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        # Displays a full summary of the account.
        info = f"--- Account Info for {self.firstname} {self.lastname} ---\n"
        info += f"Total Income:  {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Current Balance: {self.account_balance()}\n"
        info += "--------------------------------------"
        return info
    
#usage 
my_account = PersonAccount("John", "Doe")
my_account.add_income("Salary", 5000)
my_account.add_income("Freelancing", 1200)
my_account.add_expense("Rent", 1500)
my_account.add_expense("Groceries", 400)

print(my_account.account_info())

class Products:
    pass
