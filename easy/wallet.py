'''
PEDAC
--Requirements--
1. Implement a Wallet class that represents a wallet with a certain amount 
of money.
2. You want to be able to combine (add) two wallets together to get a new 
wallet with the combined total amount from both wallets.

'''

class Wallet():
    
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount
    
    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        
        total = self.amount + other.amount
        return Wallet(total)

# Examples
wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True
