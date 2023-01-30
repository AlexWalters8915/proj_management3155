### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        """More documentation for check resources"""

        if ingredients["cheese"] > self.machine_resources["cheese"]:
            print("Sorry there is not enough cheese to make your sub sandwich")
            return False
        elif ingredients["bread"] > self.machine_resources["bread"]:
            print("Sorry there is not enough bread to make your sub sandwich")
            return False
        elif ingredients["ham"] > self.machine_resources["ham"]:
            print("Sorry there is not enough ham to make your sub sandwich")
            return False
        else:
            return True

    def process_coins(self):
        total = 0
        print("How many quarters?")
        """Makes sure that there is not something like half of a quarter inputeed by casting it"""
        total += 0.25 * int(input())
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        """More informations about transaction result"""
        if coins < cost:
            print("sorry that's not enough money now refunding you.")
            return False
        if coins > cost:
            print("Here is Your " + choice + " sandwich")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        """"Improved documentation for the make_sandwhich test commit"""
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
    def report(self):
        """print current resources"""

        print("Pieces of cheese in the machine: " + str(self.machine_resources["cheese"]))
        print("pieces of ham in the machine: " + str(self.machine_resources["ham"]))
        print("Pieces of bread in the machine: " + str(self.machine_resources["bread"]))


sandwich_machine = SandwichMachine(resources)

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
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, cost):
                sandwich_machine.make_sandwich("small", recipes["small"]["ingredients"])
    if choice == "medium":
        if sandwich_machine.check_resources(recipes["medium"]["ingredients"]):
            cost = recipes["medium"]["cost"]
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, cost):
                sandwich_machine.make_sandwich("medium", recipes["medium"]["ingredients"])
    if choice == "large":
        if sandwich_machine.check_resources(recipes["large"]["ingredients"]):
            cost = recipes["large"]["cost"]
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, cost):
                sandwich_machine.make_sandwich("large", recipes["large"]["ingredients"])
