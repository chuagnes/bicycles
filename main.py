from bicycle import bicycle, bikeshop, customers

#Create 6 bicycle models
Rager = bicycle("Rager",10, 200)
Air = bicycle("Air", 4, 800)
Trusty = bicycle("Trusty", 15, 100)
Dust = bicycle("Dust", 8, 400)
Glider = bicycle("Glider", 5, 600)
Roller = bicycle("Roller", 12, 1200)

#Create 3 customers
Agatha = customers("Agatha",200)
Blake = customers("Blake",500)
Joe = customers("Joe", 1000)

#Create bike shop with 6 models and 20% markup
inventory_list = {Air: 1, Trusty: 3, Dust: 10, Rager:2, Glider: 5, Roller: 9}
Mike = bikeshop("Mike", inventory_list, .2)

#Print initial inventory
for n in Mike.inventory:
    print("{}: {}".format(n.name,Mike.inventory[n]))

#Print the bikes that each customer can purchase 
customer_list = [Agatha, Blake, Joe]
for n in customer_list:
    print("\n{}:".format(n.name))
    for b in Mike.inventory:
        if b.prodcost*(1+Mike.margin) <= n.budget:
            print(b.name)

#Each customer buys a bike.  
Agatha.buybike(Trusty, Mike)
Blake.buybike(Rager, Mike)
Joe.buybike(Glider, Mike)


