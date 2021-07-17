class Account:
    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
   
    @property
    def balance(self): 
        return sum(self._transactions) + self.amount      

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @staticmethod
    def validate_transaction(account, amount_to_add): #Account
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry connot go in dept')
        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'


    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.owner}, {self.amount})'

    
    def __add__(self, other):
        new_account = Account(owner = f'{self.owner}&{other.owner}', amount = self.amount + other.amount)
        new_account._transactions.extend(self._transactions + other._transactions)
        return new_account

    def __getitem__(self, index):
            return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance



