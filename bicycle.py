class bicycle(object):
    def __init__(self, name, weight, prodcost):
        self.name = name
        self.weight = weight
        self.prodcost = prodcost
    
class bikeshop(object):
    def __init__(self, name, inventory, margin, profit = 0):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
    
class customers(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    def buybike(self, purchased_bike, bikeshop):
        purchase_price = purchased_bike.prodcost*(1+bikeshop.margin)
        self.budget -= purchase_price
        bikeshop.profit += bikeshop.margin*purchased_bike.prodcost
        bikeshop.inventory[purchased_bike] -= 1
        print("{}, you have purchased {} for ${}. You have ${} left to spend.".format(self.name, purchased_bike.name, purchase_price, self.budget))
        print("The bikeshop, {}, has made ${} in profit and has the following bikes remaining:\n".format(bikeshop.name, bikeshop.profit))
        
        for n in bikeshop.inventory:
            print("{}: {}".format(n.name,bikeshop.inventory[n]))
    

    