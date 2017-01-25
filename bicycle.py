class Bicycle(object):
    def __init__(self, name, wheel1, wheel2, frame, manufacturer):
        self.name = name
        self.frame = frame
        self.price = 0
        self.manufacturer = manufacturer #does this have to be an input?
        if wheel1.wheel_type == wheel2.wheel_type:
            self.wheel1 = wheel1
            self.wheel2 = wheel2 
        #how to return error if the two wheels aren't the same type?
        self.prod_cost = wheel1.prod_cost + wheel2.prod_cost + frame.prod_cost
        self.weight = wheel1.weight + wheel2.weight + frame.weight  
        

class Bikeshop(object):
    def __init__(self, name, inventory, margin, profit = 0):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
        
        for bike in self.inventory:
            bike.price = bike.prod_cost * (1 + self.margin)
    
    def afford_bikes(self, customer):
        bike_list = []
        for b in self.inventory:
            if b.price <= customer.budget:
                bike_list.append(b.name)
        return bike_list
    
    def stock_inventory(self, new_inventory):
        for new_bike in new_inventory:
            for bike in self.inventory:
                if new_bike == bike:
                    self.inventory[bike] += 1
    
            
                
class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    def buybike(self, purchased_bike, bikeshop):
        self.budget -= purchased_bike.price
        bikeshop.profit += bikeshop.margin*purchased_bike.prod_cost
        bikeshop.inventory[purchased_bike] -= 1

class Wheel(object):
    def __init__(self, name, weight, prod_cost, wheel_type):
        self.name = name
        self.weight = weight
        self.prod_cost = prod_cost
        self.wheel_type = wheel_type
    
    #how to ensure that there is a total of 3 different wheel_types? is this in a different function outside the class?

class Frame(object):
    def __init__(self, weight, prod_cost):
        self.weight = weight
        self.prod_cost = prod_cost
    
    def what_material(self):
        #is there an easier way to write this loop?
        loop = True
        while loop == True:
            material = input("Is the frame made of aluminum, carbon or steel? Type A, C, or S. ")
            if material.lower() == 'a':
                self.material = 'Aluminum' 
                loop = True 
            elif material.lower() == 'c':
                self.material = 'Carbon'
                loop = True
            elif material.lower() == 's':
                self.material = 'Steel'
                loop = True
            else:
                print("Please re-enter either A, C, or S.")
                loop = False

class Manufacturer(object):
    def __init__(self, name, bike1, bike2, bike3, mfg_margin):
        self.name = name
        self.mfg_margin = mfg_margin
        self.bike1 = bike1
        self.bike2 = bike2
        self.bike3 = bike3
        
        
                
        



    

    