from bicycle import Bicycle, Bikeshop, Customer, Wheel, Manufacturer, Frame

#Create 4 wheels
sturdy = Wheel("Sturdy", 2, 100, "clincher")
slick = Wheel("Slick", 1, 150, "clincher")
modern = Wheel("Modern", 1, 150, "tubeless")
supreme = Wheel("Supreme", 1.5, 125, "tublar")

#Create 2 frames
frame1 = Frame(.5, 100)
frame2 = Frame (.75, 75)

#Create 2 manufacturers
schwinn = Manufacturer("Schwinn", "Rager","Air","Trusty", .5)
bianchi = Manufacturer("Bianchi", "Dust", "Glider", "Roller", .4)

#Create 6 Bicycle models
rager = Bicycle("Rager", sturdy, slick, frame1, schwinn) #should sturdy be in quotes?
air = Bicycle("Air", modern, modern, frame1, schwinn)
trusty = Bicycle("Trusty", supreme, supreme, frame2, schwinn)
dust = Bicycle("Dust", sturdy, sturdy, frame2, bianchi)
glider = Bicycle("Glider", slick, slick, frame2, bianchi)
roller = Bicycle("Roller", supreme, supreme, frame1, bianchi)

#Create 3 Customer
agatha = Customer("Agatha",200)
blake = Customer("Blake",500)
joe = Customer("Joe", 1000)

#Create bike shop with 6 models and 20% markup
inventory_list = {air: 1, trusty: 3, dust: 10, rager:2, glider: 5, roller: 9}
mike = Bikeshop("Mike", inventory_list, .2)

#Print initial inventory
for n in mike.inventory:
    print("{}: {}".format(n.name, mike.inventory[n]))

#Print the bikes that each customer can purchase 
customer_list = [agatha, blake, joe]
for c in customer_list:
    print(mike.afford_bikes(c))

#Prints receipt each time a customer buys a bike
def print_receipt(customer, bike, Bikeshop):
    print("{}, you have purchased {} for ${}. You have ${} left to spend.".format(customer.name, bike.name, bike.price, customer.budget))
    print("The Bikeshop, {}, has made ${} in profit and has the following bikes remaining:\n".format(Bikeshop.name, Bikeshop.profit))
    for n in Bikeshop.inventory:
        print("{}: {}".format(n.name,Bikeshop.inventory[n]))

#Each customer buys a bike.  
agatha.buybike(trusty, mike)
print_receipt(agatha, trusty, mike)
blake.buybike(rager, mike)
print_receipt(blake, rager, mike)
joe.buybike(glider, mike)
print_receipt(joe, glider, mike)


    

