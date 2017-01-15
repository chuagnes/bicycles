class bicycle(object):
    def __init__(self, name, weight, prodcost):
        self.name = name
        self.weight = weight
        self.prodcost = prodcost
        
    
class bikeshop(object):
    def __init(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    def margin(self, margin):
        prices = {}
        for i in self.bikes():
            prices[self.bikes.prodcost] = (1+margin)*self.bikes.prodcost 
    
class customers(object):
    def __init(self, name, budget):
        self.name = name
        self.budget = budget

Rager = bicycle("Rager",10, 100)
Air = bicycle("Air", 4, 200)
Trusty = bicycle("Trusty", 15, 50)
Dust = bicycle("Dust", 8, 120)
Glider = bicycle("Glider", 5, 180)
Roller = bicycle("Roller", 12, 75)
inventory_list = [Rager, Air, Trusty, Dust, Glider, Roller]
Mike = bikeshop("Mike's", inventory_list)
print("\nShop name: {0}.".format(bikeshop.name))
print("\nInventory")
print("-" * 20)
for bike in range(len(inventory_list)):
    print(inventory_list[bike])
    

       
    