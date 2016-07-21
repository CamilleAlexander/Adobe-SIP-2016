import random
def menu
items = [ "BBQ" , "Honey" , "Peanutbutter"_, "Chocolate Scauce" , "Chilli" , "Mayo" , "Gravy" , "Straberry Jam" , "Alfredo" , "Meranera Scauce" ]         
adjectives = ["Creamy" , "Crispy" , "Juicy" , "Sweet" , "Spicy" , "Tender" , "Savory" , "Salty" , "Sour" , "Rich" ]
Objects = [ "Pasta" , "Chicken" , "Eggs" , "French Toast" , "Red Velvet " , "Pizza" , "Sandwiches" , "Fish" , "Tofue" , "Mushrooms" ]

adjectives_food = len(adjectives)
food_items = len(items)
objects_food = len(object)

for i in range (10):
    adjectives_food = random.randint(0 , len(adjectives))
    food_items = random.randint (0 , len(items))
    objects_food = random.randint (0 , len(Objects))
    print(adjectives[adjectives_food] + items[food_items] + Objects[objects_food])
    

adjectives_food = food(adjectives)
random_index = random.randint len(0, adjective_food-1)
print(adjectives[random_index])

food_items = food(items)
random_index = random.randint(0, food_items-1)
print(items[random_index])                

objects_food = food(object)
random_index = random.randint(0, objects_food-1)
print(Objects[random_index])  
      
