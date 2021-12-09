class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        return(f'{self.category.center(30, "*")}\n' + 
               '{:2}  {:>12}'.format(word[0], word[1], word[2]))
    
    def get_balance(self):
        balance = 0
        for record in self.ledger:
            balance += record['amount']
        return balance
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    
    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, category_class):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category_class.category}')
            category_class.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False


def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)