import data
import sandwich_maker
import cashier

resources = data.resources
recipes = data.recipes

sandwich_machine = sandwich_maker.SandwichMachine(resources)


def main():
    while True:
        """handles off/report functions"""
        print("What would you like? (small medium large off report)")
        choice = input()
        if choice == "off":
            print("Machine now powering off.....")
            exit(0)
        if choice == "report":
            print("Now reporting the current inventory levels of the sandwich machine.......")
            sandwich_machine.report()

        """Choice regarding sub size before passing it into functions"""
        if choice == "small":
            if sandwich_machine.check_resources(recipes["small"]["ingredients"]):
                cost = recipes["small"]["cost"]
                coins = cashierInstance.process_coins()
                if cashierInstance.transaction_result(coins, cost):
                    sandwich_machine.make_sandwich("small", recipes["small"]["ingredients"])
        if choice == "large":
            if sandwich_machine.check_resources(recipes["large"]["ingredients"]):
                cost = recipes["large"]["cost"]
                coins = cashierInstance.process_coins()
                if cashierInstance.transaction_result(coins, cost):
                    sandwich_machine.make_sandwich("large", recipes["large"]["ingredients"])
        if choice == "medium":
            if sandwich_machine.check_resources(recipes["small"]["ingredients"]):
                cost = recipes["medium"]["cost"]
                coins = cashierInstance.process_coins()
                if cashierInstance.transaction_result(coins, cost):
                    sandwich_machine.make_sandwich("medium", recipes["medium"]["ingredients"])


if __name__ == "__main__":
    cashierInstance = cashier.Cashier()
    main()
