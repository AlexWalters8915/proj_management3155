class Cashier:
    def __init__(self):
        self.total = 0

    def process_coins(self):
        print("How many quarters?")
        self.total += 0.25 * int(input())
        return self.total
    def transaction_result(self, coins, cost):
        if coins >= cost:
            print("Transaction accepted, making sandwich...")
            return True
        else:
            print("Transaction declined, not enough money. Please insert " + str(cost - coins) + " more quarters.")
            return False
