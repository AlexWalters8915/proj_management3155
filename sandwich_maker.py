class SandwichMachine:
    def __init__(self, resources):
        self.resources = resources

    def make_sandwich(self, size, ingredients):
        for ingredient in ingredients:
            self.resources[ingredient] -= 1
        print("Enjoy your " + size + " sandwich!")

    def check_resources(self, ingredients):
        for ingredient in ingredients:
            if self.resources[ingredient] < 1:
                print("Sorry, we are out of " + ingredient + ".")
                return False
        return True

    def report(self):
        print("Inventory levels:")
        for ingredient, count in self.resources.items():
            print(ingredient + ": " + str(count))