class Category:
    def __init__(self, category):
        self.category = category
        self.expense = 0
        self.balance = 0
        self.ledger = []

    def check_funds(self, expense):
        if self.balance >= expense:
            return True
        else:
            return False

    def deposit(self, amount, description=None):
        if description == None:
            description = ''
        self.ledger.append({"amount":amount, "description":description})
        self.balance = self.balance + amount

    def withdraw(self, amount, description=None):
        if description == None:
            description = ''

        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
            self.balance -= amount
            self.expense += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.balance -= amount
            category.deposit(amount, f'Transfer from {self.category}')
            self.ledger.append({"amount":-amount, "description":f"Transfer to {category.category}"})
            return True
        else:
            return False
    
    def __repr__(self):
        asterisk = ''
        chart = ''
        for i in range(30-len(self.category)):
            if i % 2 == 0:
                asterisk += '*'
        top = asterisk + self.category + asterisk
        for item in self.ledger:
            amount = float(item['amount'])
            if len(item['description']) > 23:
                chart += item['description'][:23] + (format(amount, ".2f")).rjust(30-len(item['description'][:23])) + chr(10)
            else:
                chart += item['description'] + (format(amount, ".2f")).rjust(30-len(item['description'])) + chr(10)
        
        return f"{top}{chr(10)}{chart}Total: {self.balance}"

    
def create_spend_chart(categories):
    spending = [round(Category.expense,2) for Category in categories]
    heading = "Percentage spent by category\n"
    percent_chart = ''
    
    total = round(sum(spending), 2)

    percentage_list =[round((((spent/total)*10)//1)*10) for spent in spending]

    for number in range(100,-1,-10):
        percent_chart += str(number).rjust(len(str(100))) + '|'
        for percentages in percentage_list:
            if percentages >= number:
                percent_chart += ' o '
            else:
                percent_chart += '   '
        percent_chart += " \n"
    
    footer = "    " + ("-" * ((len(categories)*3) + 1)) + '\n'

    the_categories = [x.category for x in categories]

    max_length = 0
    for x in the_categories:
        if len(x) > max_length:
            max_length = len(x) 
    categs = [category.ljust(max_length) for category in the_categories]

    for category in zip(*categs):
        footer += "    " + "".join(map(lambda cat: cat.center(3), category)) + " \n"
    return (heading + percent_chart + footer).rstrip("\n")